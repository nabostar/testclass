class Korean:
    country = "Korea"

    # def __inif__(self, name, age ,address):
    #     self.name = name    # self 붙는건 객채변수
    #     self.age = age
    #     self.address = address

    @classmethod
    def trip(cls, country):
        if cls.country == country:
            print("domestic")
        else:
            print("abroad")

# kim = Korean('Hong',35,'seoul')
# women = Korean('Julia',47,'seoul')

# # Korean.name
# print(kim.name)
# print(Korean.country)
# print(kim.country)
# print(women.country)

Korean.trip('Korea')
Korean.trip('usa')