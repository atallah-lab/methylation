import requests
import json

# use these to make direct API calls to GDC
Id2Hex = { '43-6771': 'b0818bee-c32c-405c-ba09-956091fbe09b', #LUSC
           '18-5595': '628b1bc3-825b-4d0e-a4cd-57eeaf98e798', #LUSC
           '22-5471': 'bece6b8e-5d6c-4dd6-85a3-9b3a9c670aa7', #LUSC
           '39-5031': '9f20b4bc-ee09-42ef-9392-68054a7a2cfe', #LUSC
           '33-4589': '49f975ea-a1cf-4a9b-bf13-030c68cc99e4', #LUSC
           '33-4586': '376dfd27-68e8-4a1a-9c4f-5064279b2a9e', #LUSC
           '50-5931': '12ccd581-a921-41bc-bcee-4e9be54532cc', #LUAD
           '38-4631': '2483621a-4db3-41ab-aa33-b9427ea8a0af', #LUAD
           '49-4488': 'd721bfe0-90e3-415e-b9f3-1a270efa5fbb', #LUAD
           '50-5932': 'ebcba7f2-ce13-4bae-97cd-91a6b1dcd465', #LUAD
           '50-5935': '100430c8-1446-45c8-af36-b6dbb3ddd0c1', #LUAD
           'AA-3697': 'dde411b2-5d2b-4638-8149-89bc1eb3c7ad', #COAD
           'AA-3713': '57a2044d-20cc-4d02-b268-ce570a0fabe3', #COAD
           'AA-3506': '28033279-cc74-4775-afdf-2497f6ddb55c', #COAD
           'AZ-6599': 'fbb69964-f962-4b89-b59b-dd05f8faf61a', #COAD
           'A6-2686': '19d1a5fc-3ce9-4e43-a364-a4150bcf911b', #COAD
           'A6-2682': '77a44132-af22-4115-9fa2-78f2f74bf687'  #COAD
          }

case_id = Id2Hex['50-5935']

files_endpt = "https://api.gdc.cancer.gov/files"

fields = ",".join(fields)

filters={"op":"and",
 "content": [
     {"op": "in",
      "content": {"field":"cases.case_id","value":[case_id]}},
     {"op": "in",
      "content": {"field":"files.data_category","value":["DNA Methylation"]}}
     ]
}
params = {
    "filters": json.dumps(filters),
    "format": "JSON"
    }

response = requests.get(files_endpt, params = params)

_json = response.content.decode('utf8').replace("'", '"')
_data = json.loads(_json)
s = json.dumps(_data, indent=2, sort_keys=True)

print(s)