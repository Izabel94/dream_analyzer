import streamlit as st
import os
import openai
import base64

openai.api_key = os.environ.get("OPENAI_API_KEY")


def gpt3(prompt, engine='davinci', response_length=64,
         temperature=0.7, top_p=1, frequency_penalty=0, presence_penalty=0,
         start_text='', restart_text='', stop_seq=[]):
    response = openai.Completion.create(
        prompt=prompt + start_text,
        engine=engine,
        max_tokens=response_length,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop_seq,
    )
    answer = response.choices[0]['text']
    return answer


def new_func(description):
    prompt = """The following is a conversation with a Freudian dream analyst.
Human: I dreamt of my teeth falling out.
AI: This dream represents sexual repression. Teeth falling out in a dream is considered a symbol of castration and fear regarding the male genitalia. And it could relate to anxiety about sexual interaction with a partner.
Human: I dreamt of a bug infestation.
AI: Insects in your dreams usually symbolize nuisances — something is literally bugging you.
Human: I had a dream about snakes in my bed.
AI: Snakes can be a symbol of the penis.
Human:  I’ve been having this dream once every few months whereby Abie and I are not married yet (either engaged or engaged to be engaged), but he breaks up with me.
AI: When our partners appear in our unconscious projections, it usually represents some aspects of the waking relationship and how we feel about it, i.e., the wishes, fears and anxieties bound up with that person in our minds. So perhaps there are some latent worries about abandonment that haven’t been entirely processed or resolved.
Human: I had a nightmare where this stranger was trying to hurt me and then my mom stepped in to save me, but then the stranger burnt my mom with a lighter:
AI: A stranger is rarely someone totally unfamiliar to you, but instead a part of yourself that is hidden. The fire in the first dream doesn’t have to be destructive — it can also be a sign of enlightenment, purification or transformation. The lighter especially seems to indicate a spark of some new idea, and the little flame could represent unacknowledged passion or desire.
Human: Every time I get really sick, with something typically involving a fever, I dream that I’m falling in a dark space with big, life-size feathers all around me. I fall until I see a mattress in the distance that looks soft and inviting, but when I land, it’s always rock-solid.
AI: Unless you’ve got a deep unconscious desire to pursue ornithology, you likely associate plucked plumes with down comforters, pillows or puffy winter jackets. In that sense, they might suggest feelings of warmth, coziness, ease and relaxation. But when you say “life-size,” do you mean “human-size?” If so, the feathers might appear in your dreamscape as substitutions for people. As for the mattress, it could represent your support system. Its rock-hard surface might indicate a feeling or suspicion that your safety net is not as reassuring as you would like. """
    prompt += description
    answer = gpt3(prompt,
                  temperature=0.7,
                  frequency_penalty=0,
                  presence_penalty=0,
                  start_text='\nAI:',
                  restart_text='\nHuman: ',
                  stop_seq=['\nHuman:', '\n'])
    return answer

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://cdn.pixabay.com/photo/2019/11/06/14/33/moon-4606246_1280.jpg")
    }
   .sidebar .sidebar-content {
        background: url("https://cdn.pixabay.com/photo/2019/11/06/14/33/moon-4606246_1280.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title('Squatting Slavs')
st.sidebar.text("present:")
st.sidebar.title('Selection Menu')
page = st.sidebar.radio(
    "Select", ("Dream Analysis by Sigmund Freud", "Dream Analysis by Carl Jung"))


if page == 'Dream Analysis by Sigmund Freud':
    st.title('Freudian Dream Analyzer')
    description = st.text_area("Enter your dream description", '')

    if st.button("What does it mean?"):
        if description == "":
            st.error("Please enter your dream description")
        else:
            with st.spinner("Fetching response..."):
                response = new_func(description)
                st.markdown(response)


if page == 'Dream Analysis by Carl Jung':
    st.title('Jungian Dream Analyzer')
    description = st.text_area("Enter your dream description", '')

    if st.button("What does it mean?"):
        if description == "":
            st.error("Please enter your dream description")
        else:
            with st.spinner("Fetching response..."):
                response = new_func(description)
                st.markdown(response)


# Jung's version to be created!

# elif page=='Bio Generator':
#   st.title('LinkedIn Bio Generator')
#   description = st.text_area("Enter your Headline",'')

#   if st.button("Generate Bio!"):
#     if description=="":
#       st.error("Please enter your headline")
#     else:
#       with st.spinner("Fetching response..."):
#           response = openai.Completion.create(
#   engine="davinci-instruct-beta",
#   prompt= f"An application to create a description from the given LinkedIn headlines.\n###\nHeadline: \nBlockchain expert and lecturer. Fractional CTO/CIO services to tech startups.\n\nLinkedIn description:\nI am a technologist, IT leader, lecturer, and cook. I provide fractional CTO and CIO services to technology startups, helping them find the right direction for their business. I deliver talks on topics such as blockchain and cryptography to a wide variety of audiences including as a guest lecturer at the Haas School of Business.\n###\nHeadline: \nEntrepreneur, Digital Marketing Expert, Investor, Mentor, Public Speaker, Blockchain and Cryptocurrency Expert.\n\nLinkedIn description:\nI am an innovative entrepreneur with more than 11 years of experience in the digital marketing, technology and service industries. I am an active member of the startup community and have founded a couple of startups and exited one of them.\n###\nHeadline: \nStudent Entrepreneur, Machine Learning Enthusiast, Data Science Enthusiast.\n\nLinkedIn description:\nI am a student entrepreneur. I have created many projects in the fields of app development, python automation and machine learning. Am also a Data Science enthusiast and I wish to get a job in this field.\n###\nHeadline:\nE-commerce Marketing and Brand Relationship Manager at Adanola. Single point of contact skill set to drive growth.\n\nLinkedIn description:\nI am a e-commerce marketing and brand relationship manager who has a wide set of skills. I drive growth for brands, managing both online and offline marketing channels such as SEO, inbound marketing, SEM, PPC, content marketing, email campaigns, and social media. I love what I do and I hope that the career I have right now will be a great stepping stone for me.\n###\nHeadline:\n{description}\n\nLinkedIn description:",
#   temperature=0.8,
#   max_tokens=100,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0,
#   stop=["###"]
# )
#           st.markdown(response['choices'][0]['text'])
