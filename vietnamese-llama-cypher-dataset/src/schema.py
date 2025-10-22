from neo4j import GraphDatabase

class Schema:
    def __init__(self, driver):
        self.driver = driver

    def create_schema(self):
        with self.driver.session() as session:
            session.run("""
            CREATE CONSTRAINT ON (p:Person) ASSERT p.id IS UNIQUE;
            CREATE CONSTRAINT ON (pro:Province) ASSERT pro.id IS UNIQUE;
            CREATE CONSTRAINT ON (d:District) ASSERT d.id IS UNIQUE;
            CREATE CONSTRAINT ON (c:Commune) ASSERT c.id IS UNIQUE;
            CREATE CONSTRAINT ON (ad:AddressDetail) ASSERT ad.id IS UNIQUE;
            CREATE CONSTRAINT ON (o:Organization) ASSERT o.id IS UNIQUE;
            CREATE CONSTRAINT ON (e:Education) ASSERT e.id IS UNIQUE;
            CREATE CONSTRAINT ON (ph:Phone) ASSERT ph.number IS UNIQUE;
            CREATE CONSTRAINT ON (id:IdentityDocument) ASSERT id.number IS UNIQUE;
            CREATE CONSTRAINT ON (sm:SocialMedia) ASSERT sm.username IS UNIQUE;
            CREATE CONSTRAINT ON (v:Vehicle) ASSERT v.plate IS UNIQUE;
            CREATE CONSTRAINT ON (lp:LicensePlate) ASSERT lp.number IS UNIQUE;
            CREATE CONSTRAINT ON (ins:Insurance) ASSERT ins.policy_id IS UNIQUE;
            """)
            # Define relationships here
            session.run("""
            // Example of creating relationships
            // CREATE (p:Person)-[:LIVES_IN]->(c:Commune)
            // CREATE (c)-[:BELONGS_TO]->(d:District)
            // CREATE (d)-[:PART_OF]->(pro:Province)
            // You can add more relationships as needed.
            """)

# Usage
def main():
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
    schema = Schema(driver)
    schema.create_schema()
    driver.close()

if __name__ == "__main__":
    main()