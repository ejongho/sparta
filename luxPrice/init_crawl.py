import requests
from bs4 import BeautifulSoup
import numpy as np

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta  

import uuid

headers = {'User-Acdgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

def get_links_mclabels(): 
  new = "a"

def get_links_farfetch():
  menFar = [135970]
  womenFar = [135971]
  # db.crawl_far.drop()
  for far in menFar:
    requestUrl = 'https://www.farfetch.com/kr/shopping/men/'
    requestUrl += "balenciaga"
    requestUrl += "/items.aspx?view=180&category="
    requestUrl += str(far)
    data = requests.get(requestUrl, headers=headers)  
    soup = BeautifulSoup(data.text, 'html.parser')
    prdList = soup.select("._c29d78 > a")
    print(len(prdList))
    for i in range(len(prdList)):
      crawl_url = "https://www.farfetch.com"
      crawl_url += prdList[i]['href']
      db.crawl_far.update({'url' : crawl_url}, {'url' : crawl_url}, upsert=True)
    
  for far in womenFar:
    requestUrl = 'https://www.farfetch.com/kr/shopping/women/'
    requestUrl += "prada"
    requestUrl += "/items.aspx?view=180&category="
    requestUrl += str(far)
    data = requests.get(requestUrl, headers=headers)  
    soup = BeautifulSoup(data.text, 'html.parser')
    prdList = soup.select("._c29d78 > a")
    print(len(prdList))
    for i in range(len(prdList)):
      crawl_url = "https://www.farfetch.com"
      crawl_url += prdList[i]['href']
      db.crawl_far.update({'url' : crawl_url}, {'url' : crawl_url}, upsert=True)
    # db.prodcut.insert_one({'ID': siteID, 'site' : 'mclabels', 'prdID' : 'A20HJ108723100', 'brand' : 'AMI', 'imgUrl' : 'https://cdn-images.farfetch-contents.com/comme-des-garcons-wallet-logo-print-tote-bag_14770240_25014374_1000.jpg?c=2', 'price': '138000', 'origin' : 'portugal', 'prdName' : 'Coeur T-shirt'})

def crawlFarfetch() :
  crawlLists = list(db.crawl_far.find({},{'_id':0}).limit(3))
  for crawlList in crawlLists :
    requestUrl = crawlList['url']
    data = requests.get(requestUrl, headers=headers)  
    soup = BeautifulSoup(data.text, 'html.parser')
    brand = soup.select('#bannerComponents-Container > h1 > span._7dfe34 > a > span')[0].text
    price = soup.select('div._81fc25 > div > span')[0].text
    prdID = soup.select('._84497d > span')[0].text
    prdName = soup.select('#bannerComponents-Container > h1 > span._d85b45._d85b45._1851d6')[0].text
    imgUrl = soup.find("meta",  property="og:image")['content']
    siteID = uuid.uuid4().hex[:8]
    isAlready = list(db.product.find({'prdID' : prdID}))
    
    if isAlready == []:
      print("aa")
      db.product.update({'prdID' : prdID}, {'ID': siteID, 'site' : 'farfetch', 'prdID' : prdID, 'brand' : brand, 'imgUrl' : imgUrl, 'comparision' : [{'site' : 'farfetch', 'price': price}], 'prdName' : prdName}, upsert=True)
    else :
      print(prdID)
      isFarExist = list(db.product.find({'prdID' : prdID, 'comparision' : {'$elemMatch': {'site' : 'farfetch'}}}))
      print(isFarExist)
      if isFarExist == []:
        db.product.update_one({'prdID' : prdID, {'$push' : {'comparision' : {'site': 'farfetch', 'price': price}}}, False)
      else :
        db.product.update_one({'prdID' : prdID, 'comparision' : [{'site' : 'farfetch', 'price': price}]}, {'$set' : {'comparision' : {'site': 'farfetch', 'price': price}}}, False)
      

    

# db.product.update_one({'prdID' : prdID, 'comparision' : [{'site' : 'farfetch', 'price': price}]}, {'$push' : {'comparision' : {'site': 'farfetch', 'price': price}}}, False)
db.product.drop()
crawlFarfetch()
# get_links_farfetch()





brands = [
  "+39 MASQ ",
  "0/ZERO CONSTRUCTION ",
  "0909 ",
  "10SEI0OTTO ",
  "16ARLINGTON ",
  "181 ",
  "1921 ",
  "1987 SHOES ",
  "205W39NYC BY CALVIN KLEIN ",
  "26.7 TWENTYSIXSEVEN ",
  "28.5 ",
  "29-TWENTYNINE ",
  "2SHIRTSAGO ",
  "2STAR ",
  "3.1 PHILLIP LIM ",
  "360SWEATER ",
  "3X1 ",
  "40WEFT ",
  "4US CESARE PACIOTTI ",
  "5 PROGRESS ",
  "7 FOR ALL MANKIND ",
  "8PM ",
  "A.P.C. ",
  "A.S. 98 ",
  "A.TESTONI ",
  "ACNE STUDIOS ",
  "A-COLD-WALL* ",
  "ACQUA DELLE LANGHE ",
  "ACT N°1 ",
  "ACTUALEE ",
  "ADD ",
  "ADER ERROR ",
  "ADIDAS ",
  "ADIDAS BY PHARRELL WILLIAMS ",
  "ADIDAS BY RAF SIMONS ",
  "ADIDAS BY STELLA MCCARTNEY ",
  "ADIDAS Y-3 YOHJI YAMAMOTO ",
  "ADIEU PARIS ",
  "ADOLFO CARLI ",
  "AERONAUTICA MILITARE ",
  "AFTERLABEL ",
  "AGAINST MY KILLER ",
  "AGL ATTILIO GIUSTI LEOMBRUNI ",
  "AGLINI ",
  "AGNONA ",
  "AHLEM EYEWEAR ",
  "AILANTO ",
  "AINEA ",
  "AJMONE ",
  "AKÈ ",
  "ALAÏA ",
  "ALAIN MIKLI ",
  "ALANUI ",
  "ALBANO ",
  "ALBERTA FERRETTI ",
  "ALBERTO ASPESI ",
  "ALBERTO BIANI ",
  "ALBERTO GOZZI ",
  "ALBERTO GUARDIANI ",
  "ALDEN ",
  "ALDO CASTAGNA ",
  "ALDO COLOMBO ",
  "ALESSANDRA RICH ",
  "ALESSANDRO DELL'ACQUA ",
  "ALESSANDRO ENRIQUEZ ",
  "ALESSANDRO GHERARDESCHI ",
  "ALEX BEGG ",
  "ALEXANDER MCQUEEN ",
  "ALEXANDER SMITH ",
  "ALEXANDER WANG ",
  "ALEXANDRE BIRMAN ",
  "ALEXANDRE VAUTHIER ",
  "ALEXIA PARMIGIANI ",
  "ALICE + OLIVIA ",
  "ALICE MCCALL ",
  "ALLEGRI ",
  "ALLEY DOCKS 963 ",
  "ALLSAINTS ",
  "ALLUDE ",
  "ALLURE ",
  "ALMA EN PENA ",
  "ALMALA ",
  "ALMERIA ",
  "ALPHA INDUSTRIES ",
  "ALPHA STUDIO ",
  "ALTEA ",
  "ALTERNATIVE ",
  "ALVIERO MARTINI 1A CLASSE ",
  "ALVIERO RODRIGUEZ ",
  "ALYSI ",
  "ALYX ",
  "AMBUSH® ",
  "AMEN ",
  "AMI ALEXANDRE MATTIUSSI ",
  "AMINA RUBINACCI ",
  "AMIRI ",
  "AMMA ",
  "AMUSE ",
  "ANCIENT GREEK SANDALS ",
  "ANDAMANE ",
  "ANDERSON'S ",
  "ANDREA D'AMICO ",
  "ANDREA FENZI ",
  "ANDREA VENTURA FIRENZE ",
  "ANDREW MACKENZIE ",
  "ANGELEYE ",
  "ANGELO MARINO ",
  "ANIS COLLECTION MILANO ",
  "ANIYE BY ",
  "ANJUNA ",
  "ANN DEMEULEMEESTER ",
  "ANNA BAIGUERA ",
  "ANNA F ",
  "ANNA MOLINARI ",
  "ANNA NEVA COUTURE ",
  "ANNA-KARIN KARLSSON ",
  "ANNARITA N ",
  "ANNECLAIRE ",
  "ANNIE P. ",
  "ANNIEL ",
  "ANONYME ",
  "ANTICA CUOIERIA ",
  "ANTICA MURRINA ",
  "ANTON BELINSKIY ",
  "ANTONELLI FIRENZE ",
  "ANTONIO BERARDI ",
  "ANTONIO MARRAS ",
  "ANTONY MORATO ",
  "ANYA HINDMARCH ",
  "APPARIS ",
  "APUNTOB ",
  "AQUASCUTUM ",
  "AQUAZZURA ",
  "ARAGONA ",
  "ARAN CASHMERE ",
  "ARIES ARISE ",
  "ARMA STUDIO ",
  "ARMANI COLLEZIONI ",
  "ARMANI EXCHANGE ",
  "ARMANI JEANS ",
  "ART 259 DESIGN ",
  "ARTISTI E ARTIGIANI ",
  "ASFVLT SNEAKERS ",
  "ASH ",
  "ASICS ",
  "ASPESI ",
  "AT.P.CO ",
  "ATELIER CIGALA'S ",
  "ATHLEISUREWEAR BY BOSS ",
  "ATLANTIC STARS ",
  "ATTIC AND BARN ",
  "ATTICA SANDALS ",
  "ATTICO ",
  "AU SOLEIL ST TROPEZ ",
  "AUA ",
  "AURELIE BIDERMANN ",
  "AURIE L'ATELIER ",
  "AVANT TOI ",
  "AVENUE 67 ",
  "AVIU ",
  "AXEL ARIGATO ",
  "AZ COLLECTION ",
  "AZHAR ",
  "ÂME BOOTS ",
  "B. PAOLETTI ",
  "BABYLON ",
  "BACON ",
  "BACTA DE TOI ",
  "BAGNOLI SARTORIA NAPOLI ",
  "BAGUTTA ",
  "BALDUCELLI ",
  "BALENCIAGA ",
  "BALIZZA ",
  "BALLANTYNE ",
  "BALLY ",
  "BALMAIN ",
  "BANDITS DU MONDE ",
  "BAO BAO ISSEY MIYAKE ",
  "BARACUTA ",
  "BARBA ",
  "BARBARA I GONGINI ",
  "BARBATI ",
  "BARBOUR ",
  "BARENA VENEZIA ",
  "BARONIO ",
  "BARRACUDA ",
  "BARRETT ",
  "BARRIE ",
  "BARTON PERREIRA ",
  "BASE LONDON ",
  "BASE MILANO ",
  "BASTONCINO ",
  "BAUM UND PFERDGARTEN ",
  "BAZAR DELUXE ",
  "BE ABLE ",
  "BE BLUMARINE BY BLUMARINE ",
  "BE UNIQUE ",
  "BEATRICE B ",
  "BECOME ",
  "BELLWOOD ",
  "BELSTAFF ",
  "BENVENUTO ",
  "BEPOSITIVE ",
  "BERNA ",
  "BERNARD DELETTREZ ",
  "BERWICH ",
  "BEST COMPANY ",
  "BETTA CORRADI ",
  "BEVERLY HILLS POLO CLUB ",
  "BIAGIO SANTANIELLO ",
  "BIAP ",
  "BIARRITZ 1961 ",
  "BIBI LOU ",
  "BIKKEMBERGS ",
  "BILLIONAIRE BOYS CLUB ",
  "BILLIONAIRE COUTURE ",
  "BILLY LOS ANGELES ",
  "BJORG ",
  "BLACKBARRETT BY NEIL BARRETT ",
  "BLACKBOURNE ",
  "BLAUER ",
  "BLAZÉ MILANO ",
  "BLK ",
  "BLK DNM ",
  "B-LOW THE BELT ",
  "BLUGIRL ",
  "BLUMARINE ",
  "BLUNDSTONE ",
  "BOB ",
  "BOGLIOLI ",
  "BOLON ",
  "BONSAI ",
  "BORBONESE ",
  "BORRIELLO NAPOLI ",
  "BORSALINO ",
  "BOSS ATHLEISURE ",
  "BOSS CASUAL ",
  "BOTONDI ",
  "BOTTEGA MARCHIGIANA ",
  "BOTTEGA VENETA ",
  "BOTTI 1913 ",
  "BOUTIQUE MOSCHINO ",
  "BOY LONDON ",
  "BOYY ",
  "BP STUDIO ",
  "BRAND UNIQUE ",
  "BRANDO ",
  "BREMA ",
  "BRIAN BROME ",
  "BRIAN DALES ",
  "BRIC'S ",
  "BRIGITTE BARDOT ",
  "BRIGLIA 1949 ",
  "BRIMARTS ",
  "BRIO CAMICERIA ARTIGIANALE ",
  "BRIONI ",
  "BROGNANO ",
  "BROOKS BROTHERS ",
  "BROOKSFIELD ",
  "BROOS ",
  "BROUBACK ",
  "BRUNATE ",
  "BRUNELLO CUCINELLI ",
  "BRUNO ANTOLINI ",
  "BRUNO BORDESE ",
  "BRUNO PREMI ",
  "BRUTO ",
  "BUFFALO LONDON ",
  "BUILDING BLOCK ",
  "BULGARI ",
  "BULGARINI ",
  "BULLY ",
  "BURAK UYAN ",
  "BURBERRY ",
  "BUSCEMI ",
  "B-USED ",
  "BUTTERO ",
  "C2H4 ",
  "CAFÈNOIR ",
  "CALIBAN ",
  "CALLAGHAN ",
  "CALLISTO CAMPORA ",
  "CALVIN KLEIN ",
  "CALVIN KLEIN JEANS ",
  "CALVIN KLEIN PERFORMANCE ",
  "CALVIN KLEIN UNDERWEAR ",
  "CAMBIO CLOTHING ",
  "CAMERUCCI ",
  "CAMICERIA MAZZARELLI ",
  "CAMICETTASNOB ",
  "CAMOUFLAGE ",
  "CAMPER ",
  "CAMPLIN ",
  "CAMPOMAGGI ",
  "CANADA GOOSE ",
  "CANADIAN ",
  "CANADIAN CLASSIC ",
  "CANALI ",
  "CANDICE COOPER ",
  "CANTARELLI ",
  "CAPOBIANCO ",
  "CAPPELLINI ",
  "CAPRI ",
  "CAR SHOE ",
  "CARE LABEL ",
  "CARHARTT ",
  "CARLO CHIONNA ",
  "CARLO PIGNATELLI ",
  "CARMENS ",
  "CAROLINA HERRERA ",
  "CARRERA ",
  "CARUSO ",
  "CARVEN ",
  "CASADEI ",
  "CASTANER ",
  "CAZAL EYEWEAR ",
  "CECILIE BAHNSEN ",
  "CÉDRIC CHARLIER ",
  "CÉLINE ",
  "CELLAR DOOR ",
  "CESARE PACIOTTI ",
  "CHAMPION ",
  "CHANEL ",
  "CHAOS ",
  "CHARLOTT ",
  "CHARLOTTE OLYMPIA ",
  "CHIARA FERRAGNI ",
  "CHIARINI BOLOGNA ",
  "CHIE MIHARA ",
  "CHINATOWN MARKET ",
  "CHIO DI STEFANIA D ",
  "CHLOÉ ",
  "CHON ",
  "CHOPARD ",
  "CHRISTIAN LOUBOUTIN ",
  "CHRISTIAN PELLIZZARI ",
  "CHRISTIAN ROTH ",
  "CHRISTOPHER KANE ",
  "CHROME HEARTS ",
  "CHURCH'S ",
  "CIESSE ",
  "CINZIA ARAIA ",
  "CIRCOLO 1901 ",
  "CIRCUS HOTEL ",
  "CITIZENS OF HUMANITY ",
  "CL FACTORY ",
  "CLAE ",
  "CLAIRE GOLDSMITH ",
  "CLARKS ",
  "CLARYS ",
  "CLASS ROBERTO CAVALLI ",
  "CLIPS ",
  "CLOSED ",
  "COACH ",
  "COCCINELLE ",
  "CODELLO ",
  "COLIAC ",
  "COLMAR ORIGINALS ",
  "COLORED REVOLUTION ",
  "COLORS OF CALIFORNIA ",
  "COLOUR 5 POWER ",
  "COLVILLE ",
  "COMME DES FUCKDOWN ",
  "COMME DES GARÇONS ",
  "COMME DES GARÇONS PLAY ",
  "COMME DES GARÇONS SHIRT ",
  "COMMON PROJECTS ",
  "CONVERSE ",
  "COPERNI ",
  "CORAL BLUE ",
  "CORNELIANI ",
  "CORVARI ",
  "COSTUME NATIONAL ",
  "COSTUMEIN ",
  "COTAZUR BEACHWEAR ",
  "CÔTE&CIEL ",
  "COTÉLAC ",
  "COTTWEILER ",
  "COURREGES ",
  "COVERT ",
  "CP COMPANY ",
  "CRAIG GREEN ",
  "CREER CUIR PARIS ",
  "CRIME LONDON ",
  "CRISTIAN G ",
  "CRUCIANI ",
  "CRUNA ",
  "CULT ",
  "CULT GAIA ",
  "CURRENT ELLIOT ",
  "CUTLER AND GROSS ",
  "CYCLE ",
  "D.A.T.E. ",
  "D.EXTERIOR ",
  "D1 MILANO ",
  "D'ACQUASPARTA ",
  "DACUTE ",
  "DALMINE ",
  "DAMIR DOMA ",
  "DANIEL PATRICK ",
  "DANIELE ALESSANDRINI ",
  "DANIELE FIESOLI ",
  "DANSKO ",
  "DAVID BECKHAM ",
  "DAVIDSON ",
  "DE LAMP ",
  "DEK'HER ",
  "DEKKER ",
  "DEL CARLO ",
  "DELAN ",
  "DELLA CIANA ",
  "DEPARTMENT FIVE ",
  "DESA ",
  "DESIGUAL ",
  "DESOTO ",
  "DESTIN ",
  "DEUS EX MACHINA ",
  "DEXTERIOR ",
  "DI.LA3 PARI' ",
  "DIADORA ",
  "DIADORA HERITAGE ",
  "DIANE VON FURSTENBERG ",
  "DICKSON ",
  "DIESEL ",
  "DIESEL BLACK GOLD ",
  "DIESEL RED TAG ",
  "DIKTAT ",
  "DIMORA ",
  "DIOR ",
  "DIRK BIKKEMBERGS ",
  "DISNEY ",
  "DITA ",
  "DIXIE ",
  "DKNY ",
  "DNL ",
  "DOCK MASTER'S ",
  "DOCKSTEPS ",
  "DODO BAR OR ",
  "DOLCE E GABBANA ",
  "DON THE FULLER ",
  "DONDUP ",
  "DONNA SERENA ",
  "DONNAPIU' ",
  "DOPPIAA ",
  "DORIANI CASHMERE ",
  "DOROTHEE SCHUMACHER ",
  "DOU DOU ",
  "DOUCAL'S ",
  "DR. MARTENS ",
  "DRIES VAN NOTEN ",
  "DRKSHDW BY RICK OWENS ",
  "DRÔLE DE MONSIEUR ",
  "DROME ",
  "DRUMOHR ",
  "DSQUARED2 ",
  "DUNO ",
  "DUSAN ",
  "DUVETICA ",
  "E. MARINELLA ",
  "EASTPAK ",
  "ED PARRISH ",
  "EDWARD ACHOUR PARIS ",
  "EDWARD GREEN ",
  "EGGS ",
  "ELENA IACHI ",
  "ELENA MIRÒ ",
  "ELEVENTY ",
  "ELIE SAAB ",
  "ELISABETTA FRANCHI ",
  "ELLESSE ",
  "ELVIO ZANON ",
  "EMANUELA CARUSO ",
  "EMANUELE BICOCCHI ",
  "EMANUELE CURCI ",
  "EMANUELE FERRARI ",
  "EMILIO PUCCI ",
  "EMME MARELLA ",
  "EMPORIO ARMANI ",
  "ENFANTS RICHES DÉPRIMÉS ",
  "ENTRE AMIS ",
  "ENZA COSTA ",
  "EQUIPMENT ",
  "ERIKA CAVALLINI ",
  "ERMANNO DI ERMANNO SCERVINO ",
  "ERMANNO SCERVINO ",
  "ERMENEGILDO ZEGNA ",
  "ERO JACKET ",
  "ES GIVIEN ",
  "ESCADA ",
  "ESCADA SPORT ",
  "ESPADRILLES ",
  "ESSENTIEL ",
  "ETIQUETA NEGRA ",
  "ETNIA BARCELONA ",
  "ETRE CECILE ",
  "ETRO ",
  "ETTORE LAMI ",
  "EUREKA ",
  "EUREKA BY BABYLON ",
  "EUROPEAN PROJECT ",
  "EVISU ",
  "EYEPETIZER ",
  "EYTYS ",
  "ÉTUDES ",
  "ÈGOTIQUE ",
  "F**K ",
  "FABBRICA DEI COLLI ",
  "FABI ",
  "FABIANA FERRI ",
  "FABIANA FILIPPI ",
  "FABRIZIO DEL CARLO ",
  "FACETASM ",
  "FAITH CONNEXION ",
  "FAKE LONDON GENIUS ",
  "FALIERO SARTI ",
  "FAMILY FIRST MILANO ",
  "FANTABODY ",
  "FAUSTO PUGLISI ",
  "FAY ",
  "FEAR OF GOD ",
  "FEDELI ",
  "FEDERICA TOSI ",
  "FEFÈ ",
  "FENDI ",
  "FENG CHEN WANG ",
  "FENTY PUMA BY RIHANNA ",
  "FEZ ",
  "FILA ",
  "FILETTO ",
  "FILINTRAMA ",
  "FILIPPO DE LAURENTIIS ",
  "FILLING PIECES ",
  "FILOMARINO ",
  "FINAMORE ",
  "FIORI FRANCESI ",
  "FIORINA ",
  "FIORIO ",
  "FIORUCCI ",
  "FISICO ",
  "FIT ",
  "FIVE PREVIEW ",
  "FIVEUNITS ",
  "FLOWER MOUNTAIN ",
  "FORTE COUTURE ",
  "FORTE FORTE ",
  "FOSSIL ",
  "FRACOMINA ",
  "FRADI ",
  "FRAGNELLI ",
  "FRAME ",
  "FRANCESCA BELLAVITA ",
  "FRANCESCA CONOCI ",
  "FRANCESCA MERCURIALI ",
  "FRANCESCO RUSSO ",
  "FRANKIE MORELLO ",
  "FRANKLIN & MARSHALL ",
  "FRATELLI BORGIOLI ",
  "FRATELLI ROSSETTI ",
  "FREAKY NATION ",
  "FRED MELLO ",
  "FRED PERRY ",
  "FREEDOMDAY ",
  "FRENCY & MERCURY ",
  "FRU.IT ",
  "FURLA ",
  "FUTUR ",
  "FXXKING RABBITS ",
  "G!NA ",
  "G. DI G. ",
  "GABO NAPOLI ",
  "GABRIELA HEARST ",
  "GABRIELE PASINI ",
  "GAELLE PARIS ",
  "GAETANO AIELLO ",
  "GAIA D'ESTE ",
  "GALLIANO ",
  "GALLO ",
  "GANNI ",
  "GANT ",
  "GARRETT LEIGHT ",
  "GAS JEANS ",
  "GAZZARRINI ",
  "GCDS ",
  "GEAN LUC PARIS ",
  "GEDEBE ",
  "GENDER ",
  "GEOSPIRIT ",
  "GET LOST ",
  "GHERARDI ",
  "GHERARDINI ",
  "GHOUD ",
  "GI CAPRI ",
  "GIA COUTURE ",
  "GIADA BENINCASA ",
  "GIALLO POSITANO ",
  "GIAMBATTISTA VALLI ",
  "GIAMPAOLO ",
  "GIAMPAOLO ARCHIVIO ",
  "GIAMPAOLO VIOZZI ",
  "GIANFRANCO FERRÉ ",
  "GIANLUCA - L'ARTIGIANO DEL CUOIO ",
  "GIANLUCA CAPANNOLO ",
  "GIANNI CHIARINI ",
  "GIENCHI ",
  "GIMO'S ",
  "GINA GORGEUS ",
  "GIO ZUBON ",
  "GIORGIO ARMANI ",
  "GIORGIO BRATO ",
  "GIUSEPPE DI MORABITO ",
  "GIUSEPPE ZANOTTI DESIGN ",
  "GIVENCHY ",
  "GLAM STYLE ",
  "GOLD AND WOOD EYEPIECES ",
  "GOLD CASE ",
  "GOLD HAWK ",
  "GOLDEN GOOSE ",
  "GOORIN BROS ",
  "GOOSE TECH ",
  "GOSHA RUBCHINSKIY ",
  "GOTHA ",
  "GRAN SASSO ",
  "GREEN GEORGE ",
  "GREG LAUREN ",
  "GREYMER ",
  "GR-UNIFORMA ",
  "G-SHOCK WATCHES BY CASIO ",
  "GTA ",
  "GUARDAROBA ",
  "GUCCI ",
  "GUESS ",
  "GUESS BY MARCIANO ",
  "GUIDO SGARIGLIA ",
  "GUM ",
  "H2O ITALIA ",
  "H953 ",
  "HABILLÈ ",
  "HACULLA ",
  "HAFFMANS & NEUMEISTER ",
  "HAIDER ACKERMANN ",
  "HAIKURE ",
  "HALMANERA ",
  "HAND PICKED ",
  "HANITA ",
  "HAPPINESS ",
  "HAPPY SHEEP ",
  "HARMONT & BLAINE ",
  "HARRIS WHARF LONDON ",
  "HARTFORD ",
  "HAUS BY GOLDEN GOOSE ",
  "HEBE STUDIO ",
  "HELMUT LANG ",
  "HENDERSON ",
  "HENDERSON BARACCO ",
  "HENRI LLOYD ",
  "HERITAGE ",
  "HERNO ",
  "HERON PRESTON ",
  "HETREGÓ ",
  "HEVÒ ",
  "HEY DUDE ",
  "HH COUTURE ",
  "HIDE&JACK ",
  "HIGH BY CLAIRE CAMPBELL ",
  "HIGH USE ",
  "HIMON'S ",
  "HI-TEC ",
  "HOGAN ",
  "HOGAN REBEL ",
  "HOMME PLISSÉ ISSEY MIYAKE ",
  "HOSIO ",
  "HOWLIN' ",
  "HUBLOT EYEWEAR ",
  "HUDSON ",
  "HUGO BOSS ",
  "HUGO BY HUGO BOSS ",
  "HUMAN MADE ",
  "HUNTER ",
  "HYDRA CLOTHING ",
  "HYDROGEN ",
  "I AM ",
  "I LOVE POP ",
  "IBLUES ",
  "ICE ",
  "ICEBERG ",
  "ICON ",
  "IENKI IENKI ",
  "IH NOM UH NIT ",
  "IMPERFECT ",
  "IMPERIAL ",
  "IMPURE ",
  "IN MY HOOD ",
  "IN THE MOOD FOR LOVE ",
  "INCOTEX ",
  "INDIVIDUAL ",
  "INNERRAUM ",
  "INUOVO ",
  "INVICTA ",
  "IRO ",
  "ISABEL BENENATO ",
  "ISABEL MARANT ",
  "ISABEL MARANT ÉTOILE ",
  "ISABELLE BLANCHE PARIS ",
  "ISAIA ",
  "ISHIKAWA ",
  "ISLANG ",
  "ISOLA MARRAS ",
  "ISSEY MIYAKE ",
  "ITALIA INDEPENDENT ",
  "IUTER ",
  "IXOS ",
  "IZIPIZI ",
  "J BRAND ",
  "J. HOLBENS ",
  "J.W. ANDERSON ",
  "J|D JULIE DEE ",
  "J7 ",
  "JACK & JONES ",
  "JACKAL ",
  "JACOB COHEN ",
  "JACQUELINE DE YONG ",
  "JACQUEMUS ",
  "JACQUES MARIE MAGE ",
  "JAHNKOY ",
  "J'AIMÈ ",
  "JAMES PERSE ",
  "JANE BLANC PARIS ",
  "JANET SPORT ",
  "JANET&JANET ",
  "JC PLAY BY JEFFREY CAMPBELL ",
  "JDC ",
  "JEAN PAUL GAULTIER ",
  "JEANNOT ",
  "JECKERSON ",
  "JEFFREY CAMPBELL ",
  "JEJIA ",
  "JEORDIE'S ",
  "JEREMY SCOTT ",
  "JEROME DREYFUSS ",
  "JESSIE WESTERN ",
  "JIJIL ",
  "JIL SANDER ",
  "JIL SANDER NAVY ",
  "JIMMY CHOO ",
  "JIUDIT ",
  "JOHN LOBB ",
  "JOHN SHEEP ",
  "JOHN SMEDLEY ",
  "JOHN VARVATOS ",
  "JOSEPH ",
  "JOSHUA SANDERS ",
  "JOUR/NÉ ",
  "JOVONNA LONDON ",
  "JPLUS EYEWEAR ",
  "JUCCA ",
  "JUNYA WATANABE ",
  "JURTA ",
  "JUST CAVALLI ",
  "JUST DON ",
  "JUUN.J ",
  "JUVENTUS ",
  "KADOR ",
  "KALDA ",
  "KALEOS ",
  "KANGRA ",
  "KAOS ",
  "KAPPA ",
  "KAPPA KONTROLL ",
  "KARHU ",
  "KARL LAGERFELD ",
  "KAT MACONIE ",
  "KATE SPADE ",
  "KATHARINE HAMNETT LONDON ",
  "KEJO ",
  "KELTO ",
  "KENDALL + KYLIE ",
  "KENZO ",
  "KHRISJOY ",
  "KILTIE ",
  "KIRED ",
  "KITON ",
  "KO SAMUI TAILORS ",
  "KONTATTO ",
  "KOON ",
  "KRIZIA ",
  "K-SWISS SHOES ",
  "KUBORAUM ",
  "K-WAY ",
  "L(!)W BRAND ",
  "L.A L.A TEX RANCH WEAR ",
  "L.B.M. ",
  "L4K3 ",
  "LA DOUBLEJ ",
  "LA FILERIA ",
  "LA MANIA ",
  "LA MARTINA ",
  "LA PERLA ",
  "LA SELLERIE ",
  "LABORATORI ITALIANI ",
  "LACOSTE ",
  "LAMBERTO LOSANI ",
  "LAMICA ",
  "LANCASTER PARIS ",
  "LANEUS ",
  "LANVIN ",
  "LARDINI ",
  "L'ARIANNA ",
  "LAUNDRY BY SHELLI SEGAL ",
  "LAURA BIAGIOTTI ",
  "LAURENCE DACADE ",
  "L'AUTRE CHOSE ",
  "LAVENHAM ",
  "LC23 ",
  "LE BABE ",
  "LE CAPRESI ",
  "LE CARRIE BAG ",
  "LE COL GROUP ",
  "LE PARMENTIER ",
  "LE PIACENTINI ",
  "LE SARTE PETTEGOLE ",
  "LE SILLA ",
  "LE TRICOT PERUGIA ",
  "LE VOLIERE ",
  "LEATHER CROWN ",
  "LEBOLE ",
  "LEITMOTIV ",
  "LELLA BALDI ",
  "LEMAIRE ",
  "LEMARÉ ",
  "LEMARGO ",
  "LENORA ",
  "LEO PUCCI ",
  "LEQARANT ",
  "LEREWS ",
  "LES (ART)ISTS ",
  "LES BENJAMINS ",
  "LES COPAINS ",
  "LES HOMMES ",
  "LES PETITS JOUEURS ",
  "LESCA ",
  "LEVI'S ",
  "LEVI'S MADE & CRAFTED ",
  "LIDFORT ",
  "LINDA FARROW ",
  "LINEA PITTI ",
  "LIU JEANS ",
  "LIU JO ",
  "LIVIANA CONTI ",
  "LIVV ",
  "LO.WHITE ",
  "LOCAL AUTHORITY ",
  "LOEWE ",
  "LOLA CRUZ ",
  "LOLAMAY ",
  "LONGCHAMP ",
  "LONGHI ",
  "LORENA ANTONIAZZI ",
  "LORENZO MOSSA ",
  "LORIBLU ",
  "LORO PIANA ",
  "LOS ANGELES APPAREL ",
  "LOTTO ",
  "LOVE MOSCHINO ",
  "LOVE STORIES ",
  "LUBIAM ",
  "LUCA BERTELLI ",
  "LUCCHESE ",
  "LUCHINO CAMICIE ",
  "LUCIANO PADOVAN ",
  "LUCQUES ",
  "LUIGI BIANCHI MANTOVA ",
  "LUIGI BORRELLI ",
  "LUIS TRENKER ",
  "LUISA TRATZI ",
  "LULAES ",
  "LUXOTTICA ",
  "LUXURY 1939 ",
  "LYLE & SCOTT ",
  "M MISSONI ",
  "M1992 ",
  "MA.STRUM ",
  "MACCHIA J ",
  "MACKAGE ",
  "MACKINTOSH ",
  "MAESTA MILANO ",
  "MAGDA BUTRYM ",
  "MAISON 9 PARIS ",
  "MAISON CLOCHAR ",
  "MAISON FLÂNEUR ",
  "MAISON KITSUNÉ ",
  "MAISON LAFERRIÈRE ",
  "MAISON MARGIELA ",
  "MAISON MICHEL ",
  "MAISON SCOTCH ",
  "MAJESTIC ",
  "MAJESTIC ATHLETIC ",
  "MAJESTIC FILATURES ",
  "MALÌPARMI ",
  "MALLONI ",
  "MALO ",
  "MALONE SOULIERS ",
  "MALPH ",
  "MAMMUT ",
  "MANEBÍ ",
  "MANGANO ",
  "MANILA GRACE ",
  "MANILA GRACE STREET ",
  "MANIPUR ",
  "MANOKHI ",
  "MANUEL RITZ ",
  "MARA HOFFMAN ",
  "MARC BY MARC JACOBS ",
  "MARC ELLIS ",
  "MARC JACOBS ",
  "MARCELO BURLON ",
  "MARCIANO ",
  "MARCO DE VINCENZO ",
  "MARIA GRAZIA SEVERI ",
  "MARIA LUCIA HOHAN ",
  "MARIA SANTANGELO NAPOLI ",
  "MARIAGRAZIA PANIZZI ",
  "MARINA D'ESTE ",
  "MARINA RINALDI ",
  "MARINA RINALDI SPORT ",
  "MARINE SERRE ",
  "MARKUS LUPFER ",
  "MARNI ",
  "MARQUES'ALMEIDA ",
  "MARSELL ",
  "MARTINA ",
  "MARTINE ROSE ",
  "MARYLEY ",
  "MA'RY'YA ",
  "MASERATI ",
  "MASON'S ",
  "MASSIMO ALBA ",
  "MASSIMO LA PORTA ",
  "MASSIMO PIOMBO ",
  "MASSIMO REBECCHI ",
  "MATERIA PRIMA BY GOFFREDO FANTINI ",
  "MATSUDA ",
  "MAURIZIO MIRI ",
  "MAURO GRIFONI ",
  "MAX MARA ",
  "MAX MARA STUDIO ",
  "MBT ",
  "MC2 SAINT BARTH ",
  "MCM ",
  "MCQ BY ALEXANDER MCQUEEN ",
  "MD75 ",
  "ME FUI ",
  "MEDEA ",
  "MEHER KAKALIA ",
  "MELISSA ",
  "MERCI ",
  "MEROLA ",
  "MESSAGERIE ",
  "MET IN JEANS ",
  "METAMORFOSI ",
  "MEXICANA ",
  "MIA & BEVERLY ",
  "MIA BAG ",
  "MIA-IAM ",
  "MICHAEL COAL ",
  "MICHAEL KORS ",
  "MICHAEL KURRIER ",
  "MIGLIORE ",
  "MIKI THUMB ",
  "MILA SCHON ",
  "MIMÌ A LA MER ",
  "MINIMAL ",
  "MINORONZONI 1953 ",
  "MIRA MIKATI ",
  "MIRAGE CALZATURE ",
  "MISBHV ",
  "MISS BIKINI ",
  "MISS MAX ",
  "MISSONI ",
  "MITAWA ",
  "MIU MIU ",
  "MIZUNO ",
  "MOA ",
  "MODS LONDON ",
  "MOHAI ",
  "MOLI@LIMO ",
  "MOLLIS ",
  "MOLLY BRACKEN ",
  "MOLLY GODDARD ",
  "MOMA ",
  "MOMONÍ ",
  "MONCHO HEREDIA ",
  "MONCLER ",
  "MONCLER GAMME ROUGE ",
  "MONIES ",
  "MONNALISA ",
  "MONO ",
  "MONOBI ",
  "MONOGRAPHIE ",
  "MONTBLANC ",
  "MONTECORE ",
  "MONTESANTO ",
  "MOONIES ",
  "MOORER ",
  "MOOSE KNUCKLES ",
  "MORENO MARTINELLI ",
  "MORESCHI ",
  "MORGAN DE TOI ",
  "MOSCHINO ",
  "MOSCHINO SWIM ",
  "MOSCHINO UNDERWEAR ",
  "MOTHER ",
  "MOU ",
  "MQJ ",
  "MR&MRS ITALY ",
  "MR. WOLF ",
  "MRZ ",
  "MSGM ",
  "MUGLER ",
  "MUNICH ",
  "MUSEUM CLOTHING ",
  "MVM ",
  "MY GREY ",
  "MY TWIN ",
  "MYKITA ",
  "MYTHS ",
  "N°21 ",
  "NAKED WOLFE ",
  "NANA-NANA ",
  "NANNI MILANO ",
  "NANUSHKA ",
  "NAPA BY MARTINE ROSE ",
  "NAPAPIJRI ",
  "NATIONAL STANDARD ",
  "NEIL BARRETT ",
  "NENETTE ",
  "NEOUS ",
  "NERO GIARDINI ",
  "NERVURE ",
  "NEW BALANCE ",
  "NICHOLAS ",
  "NICHOLAS KIRKWOOD ",
  "NICO GIANI ",
  "NICOLAS LAINAS ",
  "NICOLE BENISTI ",
  "NICOLE BONNET PARIS ",
  "NIKE ",
  "NINA RICCI ",
  "NINALILOU ",
  "NINE IN THE MORNING ",
  "NINEMINUTES ",
  "NIRA RUBENS ",
  "NO HATS ",
  "NOIR KEI NINOMIYA ",
  "NOON GOONS ",
  "NOOVA ",
  "NORA BARTH ",
  "NORMA KAMALI ",
  "NORTH SAILS ",
  "NORTHSKULL ",
  "NOS BEACHWEAR ",
  "NOTIFY ",
  "NR ENNERRE BY NICOLA RACCUGLIA ",
  "NUDE ",
  "NUMERO00 ",
  "NUUR ",
  "OAKLEY ",
  "OAMC ",
  "OBLÒ UNIQUE ",
  "OBVIOUS BASIC ",
  "OFFICINA36 ",
  "OFFICINE CREATIVE ",
  "OFFICINE GENERALE ",
  "OFF-WHITE ",
  "OLGANA ",
  "OLIVER GOLDSMITH ",
  "OLIVER PEOPLES ",
  "OLLA PARÉG ",
  "OMC CLOTHING ",
  "ONE ",
  "ONE.0 ",
  "ONES ",
  "ONLY ",
  "ONLY & SONS ",
  "OOF ",
  "OPENING CEREMONY ",
  "ORCIANI ",
  "ORIGINAL VINTAGE ",
  "ORLANDO ORLANDINI ",
  "ORLEBAR BROWN ",
  "ORTIGNI ",
  "OSCAR DE LA RENTA ",
  "OSEREE ",
  "OTTOD'AME ",
  "OVERCOME ",
  "P.A.M. ",
  "P.A.R.O.S.H. ",
  "P448 ",
  "PACCBET BY GOSHA RUBCHINSKIY ",
  "PACO RABANNE ",
  "PAIGE ",
  "PAKERSON ",
  "PAL ZILERI ",
  "PALLADIUM ",
  "PALM ANGELS ",
  "PALOMA BARCELÓ ",
  "PALTO' ",
  "PÀNCHIC ",
  "PANTANETTI ",
  "PANTOFOLA D'ORO ",
  "PAOLO FIORILLO ",
  "PAOLO PECORA ",
  "PAOLO VITALE ",
  "PARABOOT ",
  "PARAJUMPERS ",
  "PARIS TEXAS ",
  "PARTHENOPE ",
  "PASHMINA BY GAYNOR ",
  "PASQUINI CALZATURE ",
  "PATAGONIA ",
  "PATERSON ",
  "PATRIZIA PEPE ",
  "PAUL & SHARK ",
  "PAUL FRANK ",
  "PAUL MEMOIR ",
  "PAUL SMITH ",
  "PAULA CADEMARTORI ",
  "PAULE KA ",
  "PAURA CLOTHING ",
  "PENCE ",
  "PEOPLE ",
  "PEOPLE OF SHIBUYA ",
  "PEPE JEANS ",
  "PEPEROSA ",
  "PERCENT ",
  "PERFECTION ",
  "PERONI ",
  "PERPHECTO ",
  "PERSOL ",
  "PERSONA BY MARINA RINALDI ",
  "PESERICO ",
  "PEUTEREY ",
  "PEZZOL 1951 ",
  "PHILIPP PLEIN ",
  "PHILIPPE MODEL ",
  "PHILOSOPHY ",
  "PHONZ SAYS BLACK ",
  "PICCIONE PICCIONE ",
  "PIER CURGE' ",
  "PIERANTONIO GASPARI ",
  "PIERLUIGI CAMICERIA ",
  "PIERRE HARDY ",
  "PINK MEMORIES ",
  "PINKO ",
  "PIOMBO ",
  "PIQUADRO ",
  "PIRELLI ",
  "PLAN-C ",
  "PLATOY ",
  "PLEASE FASHION ",
  "PLEATS PLEASE ISSEY MIYAKE ",
  "PLEIN SPORT ",
  "PLEIN SUD JEANIUS ",
  "PLÙS QUE MA VÌE ",
  "PMDS ",
  "POESIE VENEZIANE ",
  "POKEMAOKE ",
  "POLAROID EYEWEAR ",
  "POLICE ",
  "POLLINI ",
  "POLLY PLUME ",
  "POMANDÈRE ",
  "POMELLATO ",
  "POMME D'OR ",
  "PONS QUINTANA ",
  "PONY ",
  "POP TRADING COMPANY ",
  "POPA ",
  "PORTALURI ",
  "POWELL ",
  "PRADA ",
  "PRADA LINEA ROSSA ",
  "PRAY FOR US ",
  "PREMIATA ",
  "PREMIÈRE FEMME ",
  "PRESSURE ",
  "PRIMATE CLOTHING ",
  "PROENZA SCHOULER ",
  "PROLEATHER ",
  "PS BY PAUL SMITH ",
  "PT01 ",
  "PT05 ",
  "PULITO 1885 ",
  "PUMA ",
  "PUNTOVITA ACCESSORIES ",
  "PURIM ",
  "PYRENEX ",
  "PYREX ",
  "QASIMI ",
  "R13 ",
  "R63 ERRESESSANTATRE ",
  "RAF SIMONS ",
  "RAG & BONE ",
  "RAINS ",
  "RAME ",
  "RAPP EYEWEAR ",
  "RARY ",
  "RAS ",
  "RAVAZZOLO ",
  "RAYMONT ",
  "RE/DONE ",
  "REBECCA ",
  "REBECCA MINKOFF ",
  "RE-BRANDED ",
  "RED VALENTINO ",
  "REDEMPTION ",
  "REEBOK ",
  "REFRIGIWEAR ",
  "RE-HASH ",
  "RELIVE ",
  "RENE CAOVILLA ",
  "REPETTO ",
  "REPLAY ",
  "REPRESENT ",
  "RETOIS ",
  "RÊVER PARIS ",
  "REVERES 1949 ",
  "REVESTED ",
  "RH45 ",
  "RHUDE ",
  "RIA MENORCA ",
  "RICCARDO COMI ",
  "RICHARD OWE'N ",
  "RICHARD SMITH ",
  "RICHMOND ",
  "RICK OWENS ",
  "RINASCIMENTO ",
  "ROA ",
  "ROBERI & FRAUD ",
  "ROBERT CLERGERIE ",
  "ROBERT FRIEDMAN ",
  "ROBERTO CAVALLI ",
  "ROBERTO COLLINA ",
  "ROBERTO DEL CARLO ",
  "ROBERTO FESTA ",
  "RODO ",
  "ROGER VIVIER ",
  "ROMEO GIGLI ",
  "RONNIC ",
  "ROSÈ A POIS ",
  "ROSSI ",
  "ROSSIGNOL ",
  "ROSSOPURO ",
  "ROTASPORT ",
  "ROTATE ",
  "ROV ",
  "ROY ROGER'S ",
  "RRD ",
  "RTA ",
  "RUCO LINE ",
  "RUNDHOLZ ",
  "RUSLAN BAGINSKIY ",
  "S MAX MARA ",
  "S.MORITZ ",
  "S.W.O.R.D 6.6.44 ",
  "SACAI ",
  "SADEY ",
  "SAINT LAURENT ",
  "SAKS POTTS ",
  "SALAR ",
  "SALCO ",
  "SALONI ",
  "SALVATORE FERRAGAMO ",
  "SALVATORE PICCOLO ",
  "SALVATORE SANTORO ",
  "SAM EDELMAN ",
  "SAM RONE ",
  "SAMANTHA SUNG ",
  "SAMSONITE ",
  "SAN CRISPINO ",
  "SANDLERS ",
  "SANITA ",
  "SANTONI ",
  "SARA BATTAGLIA ",
  "SARA ROKA ",
  "SARTITUDE NAPOLI ",
  "SARTORIO ",
  "SATISFY ",
  "SAUCONY ",
  "SAVE THE DUCK ",
  "SAVIO BARBATO ",
  "SCERVINO STREET ",
  "SCHNEIDERS ",
  "SCHUTZ ",
  "SCOTCH & SODA ",
  "SEBAGO ",
  "SEBASTIANO CODA ",
  "SEE BY CHLOÉ ",
  "SEEN USERS ",
  "SEETEES ",
  "SELECTED HOMME ",
  "SELF-PORTRAIT ",
  "SEMI-COUTURE ",
  "SEMPACH ",
  "SERAFINI ",
  "SERGIO CARIGNANI ",
  "SERGIO GAVAZZENI ",
  "SERGIO LEVANTESI ",
  "SERGIO ROSSI ",
  "SERGIO TACCHINI ",
  "SERMONETA GLOVES ",
  "SE-TA ",
  "SEVENTY ",
  "SHAFT JEANS ",
  "SHIRTAPORTER ",
  "SHO LONDON ",
  "SIGERSON MORRISON ",
  "SILHOUETTE ",
  "SILVANO SASSETTI ",
  "SILVIAN HEACH ",
  "SIMON MILLER ",
  "SIMONA CORSELLINI ",
  "SIMONE ROCHA ",
  "SIMONETTA RAVIZZA ",
  "SIVIGLIA ",
  "SKAGEN ",
  "SKILL_OFFICINE ",
  "SMITH OPTICS ",
  "SNOBBY SHEEP ",
  "SO.BE ",
  "SOANI ",
  "SOCIETY ",
  "SOFIA M. ",
  "SOFIE D'HOORE ",
  "SOLOVAIR ",
  "SONIA RYKIEL ",
  "SOPHIA KOLL ",
  "SOPHIA WEBSTER ",
  "SOPHIE HULME ",
  "SOTTOMETTIMI ",
  "SPACE ",
  "SPACE STYLE CONCEPT ",
  "SPAGO DONNA ",
  "SPEKTRE ",
  "SPELL ",
  "SPERRY ",
  "SPORTMAX ",
  "SPRAYGROUND ",
  "SPRINGA ",
  "SRVZ ",
  "SSHEENA ",
  "SSS WORLD CORP ",
  "STAGNI47 ",
  "STAMPD ",
  "STAN RAY ",
  "STAND ",
  "STARCK ",
  "STAUD CLOTHING ",
  "STÉE ",
  "STEFANO CALMONTE ",
  "STEFANO MORTARI ",
  "STELLA JEAN ",
  "STELLA MCCARTNEY ",
  "STEPHEN GOOD LONDON ",
  "STEVE MADDEN ",
  "STEWART ",
  "STILE LATINO ",
  "STILL GOOD ",
  "STOKTON ",
  "STONE ISLAND ",
  "STONE ISLAND SHADOW PROJECT ",
  "STRATEGIA ",
  "STRENESSE ",
  "STUART WEITZMAN ",
  "STUDSWAR ",
  "STUSSY ",
  "SUICOKE ",
  "SUITE 191 ",
  "SUITE 19L ",
  "SUN 68 ",
  "SUNCOO ",
  "SUNDAY 21 ",
  "SUNDEK ",
  "SUNDRESS ",
  "SUNNEI ",
  "SUNSTRIPES ",
  "SUOLI ",
  "SUPER BY RETROSUPERFUTURE ",
  "SUPERDRY ",
  "SUPERGA ",
  "SUSAN ALEXANDRA ",
  "SUSYMIX ",
  "SWAROVSKI ",
  "SWATCH ",
  "SWEET MATILDA ",
  "SWORD ",
  "T BY ALEXANDER WANG ",
  "TAGLIATORE ",
  "TAGLIATORE BY PINO LERARIO ",
  "TAKE A WAY CLOTHING ",
  "TALCO ",
  "TARA JARMON ",
  "TATRAS ",
  "TELA ",
  "TELA GENOVA ",
  "TELAROSA ",
  "TERRE ALTE ",
  "THE BRIDGE ",
  "THE EDITOR ",
  "THE GIGI ",
  "THE JACK LEATHERS ",
  "THE LAST CONSPIRACY ",
  "THE M ",
  "THE NORTH FACE ",
  "THE ROW ",
  "THE SEAFARER ",
  "THE SELLER ",
  "THE VOLON ",
  "THEMOIRÈ ",
  "THEORY ",
  "THIERRY LASRY ",
  "THOM BROWNE ",
  "THOM KROM ",
  "THRASHER ",
  "TIFFANY & CO. ",
  "TIMBERLAND ",
  "TINTORIA MATTEI 954 ",
  "TIPE E TACCHI ",
  "TISSUÉ ",
  "T-JACKET ",
  "TOD'S ",
  "TOGA PULLA ",
  "TOM FORD ",
  "TOM REBL ",
  "TOMBOY ",
  "TOMMY HILFIGER ",
  "TONELLO ",
  "TORY BURCH ",
  "TOSCA BLU ",
  "TPN ",
  "TRAIANO ",
  "TRANSIT ",
  "TRICKER'S ",
  "TRIPPEN ",
  "TRUE DECADENCE ",
  "TRUE ROYAL ",
  "TRUENYC ",
  "TRUSSARDI ",
  "TRUSSARDI JEANS ",
  "TUMI ",
  "TURQUOISE ",
  "TWENTY EASY BY KAOS ",
  "TWENTY FOURHAITCH ",
  "TWENTY8TWELVE ",
  "TWINS BEACH COUTURE ",
  "TWIN-SET ",
  "TWO DENIM ",
  "U.P.W.W. ",
  "U.S. POLO ASSN. ",
  "UGG ",
  "ULLA JOHNSON ",
  "ULTRÀCHIC ",
  "UMBRO ",
  "UNA VOX ",
  "UNDERCOVER ",
  "UNFORTUNATE PORTRAIT ",
  "UNGARO ",
  "UNIFORM ",
  "UNISA ",
  "UNITED STANDARD ",
  "UNRAVEL PROJECT ",
  "UP TO BE ",
  "UZURII ",
  "V.D.P. ",
  "VALDITARO ",
  "VALENTINO ",
  "VALENTINO BY MARIO VALENTINO ",
  "VALENTINO GARAVANI ",
  "VALSPORT ",
  "VANDOM ",
  "VANGHER N.7 ",
  "VANS ",
  "VEJA ",
  "VENGERA ",
  "VERDERA ",
  "VERSACE ",
  "VERSACE COLLECTION ",
  "VERSACE JEANS ",
  "VERSUS VERSACE ",
  "VESTI L'ARTE ",
  "VETEMENTS ",
  "VIA MASINI 80 ",
  "VIA ROMA 15 ",
  "VIADESTE ",
  "VIC BY VIC MATIÉ ",
  "VIC MATIÉ ",
  "VICTORIA BECKHAM ",
  "VICTORIA'S SECRET ",
  "VICTORY BOAT ",
  "VIDORRETA ",
  "VIKI-AND ",
  "VILA CLOTHES ",
  "VINCE ",
  "VINCENZO BUCCI ",
  "VINTAGE DE LUXE ",
  "VIONNET ",
  "VISION OF SUPER ",
  "VISVIM ",
  "VITA FEDE ",
  "VIVETTA ",
  "VOGUE EYEWEAR ",
  "VOILE BLANCHE ",
  "VOJD STUDIOS ",
  "VOLANTIS ",
  "VOLFAGLI ",
  "W LES FEMMES BY BABYLON ",
  "WAII ",
  "WANDERING ",
  "WANDLER ",
  "WAY? ",
  "WEB EYEWEAR ",
  "WEEKEND BY MAX MARA ",
  "WEILI ZHENG ",
  "WEILL ",
  "WELL AGED ",
  "WEXFORD ",
  "WHAT FOR ",
  "WHITE SAND ",
  "WHITESAND ",
  "WHO'S WHO ",
  "WHYCI ",
  "WINDSOR SMITH ",
  "WIZE & OPE ",
  "WLNS WELLNESS CASHMERE ",
  "WOLF TOTEM ",
  "WOMSH ",
  "WOOL & CO ",
  "WOOLRICH ",
  "WUSHU RUYI ",
  "XACUS ",
  "Y/PROJECT ",
  "YAN SIMMON ",
  "YATAY ",
  "YEEZY ",
  "YERSE ",
  "YNOT? ",
  "YOHAN KIM ",
  "YOHJI YAMAMOTO ",
  "YOSH COLLECTION ",
  "Z ZEGNA ",
  "ZANELLA ",
  "ZANELLATO ",
  "ZANONE ",
  "ZESPA ",
  "ZHELDA ",
  "ZIMMERMANN ",
  "ZIVIANI ",
  "ZOE ",
  "ZOE JORDAN ",
  "ZOE KARSSEN "
]

categories = ["Coats", "Dresses", "Jackets", "Jeans", "Jumpsuits", "Knitwear", "Lingerie & Swimwear", "Outerwear Jackets", "Polo Shirts", "Shirts", "Shorts","Skirts", "Sweatshirts", "T-shirts", "Tops", "Pants", "Ankle Boots", "Boots", "Flats", "Heels", "Lace-Up Shoes", "Loafers", "Sandals", "Sneakers","Wedges", "Backpacks", "Belt Bags", "Briefcases", "Clutches", "Handbags", "Shopping Bags", "Shoulder Bags", "Travel Bags", "Bag's Accessories", "Belts & Braces", "Jewelry", "Glasses", "Gloves", "Hair Accessories", "Hats", "High Tech", "Keyrings", "Scarves & Foulards","Socks","Wallets","Watches","Other Accessories", "Suits", "T-shirts", "Underwear & Swimwear", "Messenger Bags", "Ties & Bowties"]

# data = requests.get('https://www.mclabels.com/search?type=product&q=gucci*&_=pf&pf_pt_category=ankle%20boots', headers=headers)  
# soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)
# print(soup.select('article'))
# crawl_url = soup.select('article')
# db.url_mc.insert_one({'url' : crawl_url)}





# mclabels 에서 url 크롤링할 때
# for brand in brands:
#   for category in categories:
#     requestUrl = 'https://www.mclabels.com/search?type=product&q='
#     requestUrl += brand
#     requestUrl += "*&_=pf&pf_pt_category="
#     requestUrl += category
#     data = requests.get(requestUrl, headers=headers)  
#     soup = BeautifulSoup(data.text, 'html.parser')
      # db.prodcut.insert_one({'ID': siteID, 'site' : 'mclabels', 'prdID' : 'A20HJ108723100', 'brand' : 'AMI', 'imgUrl' : 'https://cdn-images.farfetch-contents.com/comme-des-garcons-wallet-logo-print-tote-bag_14770240_25014374_1000.jpg?c=2', 'price': '138000', 'origin' : 'portugal', 'prdName' : 'Coeur T-shirt'})

    # db.url_mc.insert_one({'url' : 
  


# mclabels에서 크롤링할 때 필요한 값들
# data = requests.get('https://www.mclabels.com/collections/0-zero-construction/products/0zero-construction-blue-jeans', headers=headers)
# soup = BeautifulSoup(data.text, 'html.parser')
# price = soup.select('.actual-price')[0].text
# prdID = soup.select('div.product-page--description > div > ul > li:nth-child(5)')[0].text.replace("product code ", "")
# brand = soup.select('div.product-page--title-n-vendor > h1 > a')[0].text
# imgUrl = soup.select('.lazypreload')[0][]
# print(imgUrl)
# site = "mclabels"
# prdName = soup.select('.product-page--title').text
