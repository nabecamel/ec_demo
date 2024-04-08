from app import models
from common.database import factories


class ProductSeeder:
    DEFAULT_UUIDS = [
        'c12e77ad-5594-4b74-a387-9f2ddaa7dd40',
        'a12e9edf-6bd9-4200-a9b4-a609f9a0dc66',
        '649c029c-a621-4b95-bad1-cde56b57cc21',
        '048f4880-f76f-4f9e-b93b-9a5833e50c8f',
        '5ce424c3-e3ce-4ed1-ab48-840c91fc04ea',
        'fe516c93-f989-497d-a627-0d75fa79d576',
        '780dab76-5d06-436d-b0a5-b86edb82056a',
        '23ac17d2-8bd8-43f7-99a1-e7ee8cc0d212',
        '6e9427f9-33bf-4523-bf11-a3ab61a79d71',
        'df713d5a-1d9c-496c-8d22-b89bfe83ccd7',
        '24caf9f4-eb07-4837-92da-666b7525c9cd',
        '3bc69947-df27-4849-9114-86c7922da4bb',
        'e82c2bab-a7cd-4c67-b4a4-f4212bb4f81a',
        'ad5bb81e-2bf6-480d-94db-884d349a8ef9',
        'a16b6ea2-8ae7-4a1e-a5f6-3df8f4f6f7c3',
        '985be571-03a8-41ac-90a2-08113491af4e',
        'b2b58883-4fe2-456e-91f0-adae8f5b6cfe',
        '92333779-dd85-42d4-982f-571841623c43',
        '7bbaa041-d363-475f-aae9-ece46de8cd33',
        '1f5e2e0d-5c5c-4d6e-8f6d-3b7f8d7d8d8d'
    ]

    
    def handle(self):
        i = 0
        for uuid in ProductSeeder.DEFAULT_UUIDS:
            factories.ProductFactory.create(
                code = uuid,
                name = f"product{i}",
                unit_price = 100 * 1,
                percent_tax = 5
            )
            i+=1
