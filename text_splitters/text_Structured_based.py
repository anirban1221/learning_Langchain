from langchain_text_splitters import RecursiveCharacterTextSplitter
text="""Real Madrid Club de Fútbol (Spanish pronunciation: [reˈal maˈðɾið ˈkluβ ðe ˈfuðβol] ⓘ), commonly referred to as Real Madrid, is a Spanish professional football club based in Madrid. The club competes in La Liga, the top tier of Spanish football.

Founded in 1902 as Madrid Football Club, the club has traditionally worn a white home kit since its inception. The honorific title 'Real' is Spanish for "Royal" and was bestowed to the club by King Alfonso XIII in 1920 along with the crown in the club crest. Real Madrid have played their home matches in the 78,297-capacity Santiago Bernabéu in Madrid since 1947. Unlike most European sporting clubs, Real Madrid's members (socios) have owned and operated the club throughout its history. The official Madrid anthem is the "Hala Madrid y nada más", written by RedOne and Manuel Jabois.[8] The club is one of the most widely supported in the world and is the most followed football club on social media according to the CIES Football Observatory as of 2024.[9][10] It was estimated to be worth $6.6 billion in 2024, making it the world's most valuable football club.[11] In 2024, Real Madrid became the first football club to make €1 billion ($1.08bn) in revenue according to the club's announcement.[12]

Real Madrid are one of the most successful football clubs in the world and most successful in Europe. In domestic football, the club has won 71 trophies; a record 36 La Liga titles, 20 Copa del Rey, 13 Supercopa de España, a Copa Eva Duarte and a Copa de la Liga.[13] In International football, Real Madrid have won a record 35 trophies: a record 15 European Cup/UEFA Champions League titles, a record six UEFA Super Cups, two UEFA Cups, a joint record two Latin Cups, a record one Iberoamerican Cup, and a record nine FIFA Club World championships.[note 1] Madrid was ranked joint first a record number of times in the International Federation of Football History & Statistics (IFFHS) Club World Ranking for the years 2000, 2002, 2014, 2017, and 2024.[17] In UEFA, Madrid ranks first in the all-time club ranking.[18][19] 
"""
splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)
chunks=splitter.split_text(text)
print(len(chunks))
print(chunks)