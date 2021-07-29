from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"country_name":"Mozambique", "country_code":"+258", "ISO_Code_alpha2":"MZ", "ISO_Code_alpha3":"MOZ", "languages": [
        "portuguese", "Changana", "Bitonga", "Ronga", "Makhuwa", "Nyanja", "Ndau", "Sena", "Chwabo", "Tswa"],
        "_links":[{"Wikipedia":"https://www.wikiwand.com/en/Mozambique"}],
     "official_language":"Portuguese", 
     "provinces":[{"Maputo Cidade":
     [{
         "population":"1,456,536.00",
         "area":"347.69Km2",
         "districts":["KaMpfumo", "Chamanculo", "Maxaquene", "Mavota", "Mubukwane", "Catembe", "Inhaca"],
         "_links":[{"wikipedia":"https://www.wikiwand.com/en/Maputo", "government_official":"https://www.cmaputo.gov.mz/"}]
         
     }],"Maputo Provincia":[], "Gaza":[], "Inhambane":[],"Sofala":[], "Manica":[], "Tete":[], "Zambezia":[], "Nampula":[],"Niassa":[],"Cabo Delgado":[]}]}

@app.get("/languages")
async def get_languages_list():
    return [
        "portuguese", "Changana", "Bitonga", "Ronga"
    ]