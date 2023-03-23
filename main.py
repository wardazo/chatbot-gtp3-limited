import streamlit as st
import openai
from streamlit_chat import message

openai.api_key = st.secrets["APIKEY"]

prompt = """
I am a question answering bot. I can only answer questions about the dataset below. If you ask me a question outside the dataset, I will respond with 'Sorry I dont know [this issue] , Ill pass you to an agent'. 

Q: How do I make a reservation?
A: Click the "Booking" button, choose your type of cabin(s), your travel dates on the calendar, and the system will guide you to reserve your cabin(s). Once done, you will immediately receive an email indicating all the details, including where to send the payment. We will wait up to 24 hours (only for bookings more than 15 days in advance; for less than 15 days in advance we will wait 2 hours) for you to make that wire transfer; In that period of time, you will keep your spaces blocked. Upon receipt of proof of payment, we will definitively confirm your reservation and send you the receipt and the corresponding sales slip. Fast and easy!;
Q: Is breakfast included in the price of the little cabins?
A: No, breakfast is not included but, if you wish (and we recommend it!) you can include it at the end of the booking process for an additional value.;
Q: What are the Check-In and Out times?
A: Check IN: from 15:00 hrs (3PM) to 23:00 hrs (11PM) - Check Out: 11:00 hrs (11AM);
Q: Is there a cell phone signal in the Lodge Caleta Gonzalo sector? And in the Pumalín Park?
A: The cell phone signal in the area where the Caleta Gonzalo Lodge is located is very weak and will depend on the physical place where you are. In general in the sector of cabins and surroundings of the restaurant there is enough signal for messaging (WhatsApp and email). Movistar and Wom have good coverage. Entel allows 2G.&nbsp;There is no cell phone coverage in the areas of the trails, with the exception of some points in height and clear geography (such as hilltops). The general rule is that you plan your hikes assuming that there will be no cell phone signal.;
Q: Is there wifi in the logde?
A: We cannot offer Wifi to our guests. We only have satellite internet that covers the basic administrative and commercial needs of the Lodge. In any case, in the event of any emergency or very urgent need, we will be happy to help you by sharing with you one of our computers that is connected to the satellite.;
Q: How do I pay for services at the Lodge? Should I bring cash? Do you accept credit cards? Are there ATMs?
A: At Lodge Caleta Gonzalo we are connected to the internet via satellite, which allows us to accept credit or debit cards. That being said, these types of connections fail on some occasions (especially in rainy and windy weather) and that is why we suggest bringing cash. The closest ATMs are in Hornopirén and Chaitén.;
Q: Where can I get fuel?
A: If you go to Lodge Caleta Gonzalo you will find fuel stations in Hornopirén, Chaitén and El Amarillo. We always recommend filling your tank when you find a service station!;
Q: What happens if I have to cancel my already paid trip?
A: In those cases, we will apply the cancellation charges established in our <a href="https://lodgecaletagonzalo.cl/en/terms-conditions/">TERMS &amp; CONDITIONS</a>. It is important that you read them and agree with them.;
Q: The little cabins do not have a kitchen: where can we have lunch or dinner?
A: The cabins are located very close to the Lodge's restaurant/cafeteria. Here breakfasts, lunches and dinners are served for our guests. The restaurant offers a "daily menu" for both lunch and dinner. We have an interesting wine list and our pastries are very well known! We also have a “box-lunch” or “packed lunch” that is very practical for those who go out for a hike after breakfast, walk the trails of Pumalín during the day and return in the afternoon/evening to have dinner and relax.&nbsp;We have 2 cabins that do have a kitchen: Colonos and the Hobbit Villa. If you want a "shot" of nature and tranquility, these are your best alternatives. These little cabins are far from the parking lot, app. 400-500 meters and therefore you have to walk a little to get to them... but that little effort is largely rewarded with the location!;
Q: Do I have to pay an entrance fee to walk the trails of the Pumalín Douglas Tompkins National Park?
A: No. The Pumalín Park is crossed by Route 7 (Carretera Austral) and all its trails start from this route. CONAF -unitl now- does not charge for accessing these trails.;
Q: I want to go camping at any of the campsites in Pumalín. Should I book with you?
A: Lodge Caleta Gonzalo manages the <a href="https://lodgecaletagonzalo.cl/en/camping-2/">Río Gonzalo campsite</a>, located in Caleta Gonzalo. This is a campsite with no vehicular access - only tents, no motorhomes nor mobile homes allowed - and it is an ideal place as a base for trekking on the Cascada trail (150 meters away), 13 kms away from the Alerce and Tronador trails and 17 kms from Cascadas Escondidas trail.;Camping Río Gonzalo MUST be reserved on our platform on this same website.All the other campsites in Pumalin (Cascadas Escondidas, Lago Blanco, Lago Negro, Volcán and in the Amarillo sector: Ventisquero and Camping Grande) are all managed by CONAF, they do not have a reservation system and their access is by order of arrival. ;For more and better information in this regard, contact parque.pumalin@conaf.cl and/or telephone 652203107 or 652436337 during office hours 8:30 a.m. to 5:30 p.m. Monday through Sunday.
Q: I want to get on the ferry? is it enough to arrive and they will embark me or do I need to book in advance? Can you make that reservation?
A: It is very important that you have your reservation made well in advance. There is a high demand for this service and you do not want to run out of tickets for your vehicle and your travel group. We do not make these reservations but here we give you the info so you can do it directly online: For the Bimodal route (Hornopirén-Leptepu-Fiordo Largo-Caleta Gonzalo and vice versa) you must book online with <a href="https://www.barcazas.cl/barcazas/comprar-pasaje-hornopiren-caleta-gonzalo/">SOMARCO</a>. For the Puerto Montt-Chaitén or Chiloé-Chaitén route (and vice versa) you must book online with <a href="https://navieraustral.cl/">NAVIERA AUSTRAL</a>.;
Q: How do I book a flight to go from Puerto Montt to Chaitén? and how can I go from there to Lodge Caleta Gonzalo?
A: Flying to Chaitén is an excellent alternative! Flights depart from La Paloma aerodrome in Puerto Montt and land in Santa Bárbara, minutes from Chaitén. The flight takes about 20 minutes. You can contact <a href="https://www.pewenchile.com/">PEWEN</a> or <a href="https://www.aerocord.cl/">AEROCORD</a>. At the Santa Bárbara aerodrome you can take a taxi to Caleta Gonzalo. If that's the case, let us know and we can coordinate a ride for you.;
Q: Can I go with my pets to the National Parks?
A: Their entry is not allowed since, in addition to disturbing wildlife, they can transmit and spread diseases. In turn, pets can also contract diseases typical of wildlife.;
Q: How is the access to the loft of the cabins that have it?
A: Some of our cabins have a loft where one or two single beds are located (cabins for 3, 4 and 5 people). These lofts were designed thinking that they will be used by children, teenagers and adults with good physical capacity; access to this loft is through a vertical ladder whose use requires that users who want to go up or down from the loft have good mobility. Additionally, this loft has a very low height so it is not possible to stay fully upright while in the loft. ;We do NOT recommend these loft beds for people with mobility issues or the elderly. Climbing up and down this ladder requires a certain level of mobility and strength and a lack of this could cause a fall with the physical consequences associated with this type of accident. If you don't want to have those complications, please consider using the bed(s) on the first floor or reserving another cabin;
Q: [INPUT]
A: 
"""

st.header("Chatwith GTP3 Demo")
st.markdown("GTP3")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def query(payload):
    p = prompt.replace('[INPUT]',payload)
    response = openai.Completion.create(
        model="text-davinci-003",
        temperature=0,
        prompt=p,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )

    print(response['choices'])

    return response['choices'][0]['text']


def get_text():
    input_text = st.text_input("chat", key="chat")
    return input_text


user_input = get_text()

message("Hi! How can I help?")


if user_input and user_input != "":

    st.session_state.past.append(user_input)
    st.session_state.generated.append(query(user_input))

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))

