import json
from django.http import JsonResponse
from django.db import connections


def geodata(_):
    with connections['default'].cursor() as cursor:
        # Execute the SQL query to retrieve the data from the database
        cursor.execute(
        """
        SELECT
        jsonb_build_object(
            'type',       'Feature',
            'geometry',   ST_AsGeoJSON(ST_Force2D(ST_Transform(troncon_de_route.geometrie, 4326 )))::jsonb,
            'properties', jsonb_build_object(
                'longueur (m)',             ST_Length(ST_Transform(troncon_de_route.geometrie, 4326 )::geography),
                'vitesse_moyenne_vl (km/h)', troncon_de_route.vitesse_moyenne_vl,
                'code_postal', troncon_de_route.insee_commune_gauche)
        ) AS json
        FROM troncon_de_route
        WHERE troncon_de_route.insee_commune_gauche = '97416'
        """
        )

        # Fetch the data from the cursor
        data = cursor.fetchall()

        
        # Calculate the "tta" value
        results = []
        for row in data:
            # get json data
            geojson = json.loads(row[0])
            
            length = geojson['properties']['longueur (m)']
            vitesse_moyenne_vl = geojson['properties']['vitesse_moyenne_vl (km/h)']
            tta = round((length / 1000) / (vitesse_moyenne_vl + 1) * 3600)
            
            geojson['properties']['tta (s)'] = tta
            
            results.append(geojson)

    # Return the results in a JSON response
    return JsonResponse(results, safe=False)

