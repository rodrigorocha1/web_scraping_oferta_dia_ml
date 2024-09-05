import re

url = "https://www.mercadolivre.com.br/apple-iphone-13-128-gb-rosa-distribuidor-autorizado/p/MLB1018500849?pdp_filters=deal:MLB779362-1001&hide_psmb=true#wid=MLB2627750538&sid=search&promotion_type=TODAY_PROMOTION&searchVariation=MLB1018500849&deal_print_id=07fb9695-51bf-45ad-bb9a-b4a69a033d98-n&position=34&search_layout=grid&type=product&tracking_id=b4fe3aab-3857-4809-a1fc-dfa770857031&deal_print_id=4fbf4448-5a28-4941-acf5-c9347a8c1b85&promotion_type=TODAY_PROMOTION"


match = re.search(r'/([A-Z0-9]+)\?', url)
print(match)
if match:
    value = match.group(1)
    print("Valor encontrado:", value)
else:
    print("Valor não encontrado")
