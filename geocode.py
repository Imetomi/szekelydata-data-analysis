import geocoder
from unidecode import unidecode

def check_lang(place):
	place = place.lower()
	place = unidecode(place)

	if place == "parajd":
		place = "praid"

	elif place == "csikszereda" or place == "miercurea-ciuc" or place == "miercurea ciuc" or place=="csiktaploca" or place == "taplota-ciuc":
		place = "Miercurea Ciuc"
        
	elif place == "kezdi" or place == "kezdivasarhely":
		place = "Targu Secuiesc"

	elif place == "cristur" or place == "keresztur":
		place = "Cristuru Secuiesc"

	elif place == "ditro":
		place = "Ditrău"

	elif place == "balanbanya":
		place = "Bălan"

	elif place == "csikszentdomokos":
		place = "Sândominic"

	elif place == "udvarhely":
		place = "Odorheiu Secuiesc"

	elif place == "gyergyo" or place == "gyergyoszentmiklos":
		place = "Gheorgheni"

	elif place == "szentgyorgy" or place == "sepsiszentgyorgy":
		place = "Sftantu Gheorge"

	elif place == "szentegyhazasfalu" or place == "vlahica" or place == "vlahita":
		place = "Vlăhița"

	elif place == "segesvar":
		place = "Sighișoara"

	elif place == "homorodszentmarton":
		place = "Martiniș"

	elif place == "jedd":
		place = "Livezeni"

	elif place == "barot":
		place = "Baraolt"

	elif place == "martonfalva":
		place = "Metiș"

	elif place == "alsoboldogfalva":
		place = "Bodogaia"

	elif place == "nyikomalomfalva":
		place = "Morăreni"

	elif place == "homorodalmas":
		place = "Merești"

	elif place == "szekelyszenterzsebet":
		place = "Eliseni"

	elif place == "kezdiszentlelek":
		place = "Sânzieni"

	elif place == "ikafalva":
		place = "Icafalău"

	elif place == "csikrakos":
		place = "Racu"

	elif place == "szilagysomlyo":
		place = "Șimleu Silvaniei"

	elif place == "szentkatolna":
		place = "Catalina"

	elif place == "gyergyoremete":
		place = "Remetea"

	elif place == "kilyenfalva":
		place = "Chileni"

	elif place == "nyujtod":
		place = "Lunga"

	elif place == "ssiktaploca":
		place = "Csikszereda"

	elif place == "gyergyoalfalu":
		place = "Joseni"

	elif place == "felsofalva":
		place = "Ocna de Sus"

	elif place == "szentabraham":
		place = "Avrămești"

	elif place == "kisbacon":
		place = "Bățanii Mici"
    
	elif place == "ozsdola":
		place = "Ojdula"
        
	elif place == "csikszentimre":
		place = "Sântimbru"
        
	elif place == "csikszentsimon":
		place = "Sânsimion"
    
	elif place == "Kissolymos":
		place = "Șoimușu Mic"

	elif place == "marosszentgyorgy":
		place = "Sângeorgiu de Mureș"             
        
	elif place == "erdofule":
		place = "Filia"

	elif place == "kelementelke":
		place = "Călimănești"
        
	elif place == "felsoboldogfalva":
		place = "Feliceni"
        
	elif place == "csikszentmarton":
		place = "Csikszentmàrton"
        
	elif place == "csomafalva":
		place = "Ciumani"
        
	elif place == "kapolnasfalu":
		place = "Căpâlnița"
        
	elif place == "bibarczflava":
		place = "Biborțeni"
        
	elif place == "nyaradszereda":
		place = "Miercurea Nirajului"
        
	elif place == "rugonfalva":
		place = "Rugănești"
        
	elif place == "homorodszentpal":
		place = "Sânpaul"
        
	elif place == "agyagfalva":
		place = "Lutița"
        
	elif place == "szotyor":
		place = "Coșeni"
        
	elif place == "olasztelek":
		place = "Tălișoara"
        
	elif place == "lemheny":
		place = "Lemnia"
        
	elif place == "nagygalambfalva":
		place = "Porumbenii Mari"
        
	elif place == "disznajo":
		place = "Vălenii de Mureș"
        
	elif place == "csikszenttamas":
		place = "Tomești"
        
	elif place == "zetelaka":
		place = "Zetea"
        
	elif place == "magyarhermany":
		place = "Herculian"
        
	elif place == "csikszentmiklos":
		place = "Nicolești"
        
	elif place == "andrasfalva":
		place = "Măneuți"
        
	elif place == "tekeropatak":
		place = "Valea Strâmbă"
        
	elif place == "kukullokemenyfalva":
		place = "Târnovița"
        
	elif place == "kaszonaltiz":
		place = "Plăieșii de Jos"
        
	elif place == "alsocsernaton" or place == "felsocsernaton":
		place = "Cernat"
        
	elif place == "mikoujfalu":
		place = "Micfalău"
        
	elif place == "magyarhetmany":
		place = "Herculian"
        
	elif place == "ujszekely":
		place = "Secuieni"
        
	elif place == "farkaslaka":
		place = "Lupeni"
        
	elif place == "futasfalva":
		place = "Alungeni"
        
	elif place == "szarazajta":
		place = "Aita Seacă"
        
	elif place == "szekelyszaldobos":
		place = "Doboșeni"
        
	elif place == "zetevaralja":
		place = "Sub Cetate"
        
	elif place == "Jenofalva":
		place = "Ineu"

	elif place == "szarhegy":
		place = "Lazarea"

	elif place == "cluj-napoca" or place == "cluj napoca" or place == "kolozsvar":
		place = "Cluj Napoca"

	elif place == "regen":
		place = "reghin"
        
	elif place == "targu-mures" or place == "vasarhely" or place == "marosvasarhely" or place == "targu mures":
		place = "Targu Mures"
        
	return place.lower()


def decode(place):
	data = geocoder.arcgis(str(place))
	if data.address is not None:
		result = [data.latlng[0], data.latlng[1], data.address.split(', ')[0]]
		return result