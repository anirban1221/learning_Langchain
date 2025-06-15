from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict
import os

load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528", 
    task="text-generation",
    huggingfacehub_api_token=hf_token
)

model = ChatHuggingFace(llm=llm)

# schema
class Review(TypedDict):
    summary:str
    sentiment:str

structured_model=model.with_structured_output(Review)

Prompt=""" 
You are a helpful assistant that  summarizes movie reviews.

Return the output in the following JSON format:
{
   "summary":"...",
   "sentiment":"positive" or "negative" or "neutral"
}
Review:
"Mission: Impossible - The Final Reckoning": A Thrilling (and Potentially Final) Ride for Ethan Hunt
Christopher McQuarrie's "Mission: Impossible - The Final Reckoning," the highly anticipated eighth installment in the beloved franchise, delivers precisely what fans have come to expect: a pulse-pounding, visually stunning, and emotionally resonant cinematic experience. Having premiered in Tokyo and screened at Cannes, early critical reception is largely positive, praising its grand scale and Tom Cruise's undiminished commitment to practical, jaw-dropping stunts.
From the outset, "The Final Reckoning" establishes a clear sense of urgency and higher stakes than ever before. Ethan Hunt (Tom Cruise) and the IMF team are thrust into a new, existential threat that genuinely feels world-ending. The narrative, while at times dense, is propelled forward by a relentless pace, ensuring that audiences are constantly on the edge of their seats. The film masterfully balances intricate plot points with the signature, exhilarating action sequences that are the very bedrock of the "Mission: Impossible" legacy.
Speaking of action, this film elevates the bar yet again. Cruise, now in his early 60s, continues to defy expectations, performing stunts that would make lesser mortals balk. Reviewers are quick to highlight the breathtaking practical effects and inventive choreography, noting that the sheer spectacle of these moments is reason enough to see the film on the biggest screen possible. It's a testament to the franchise's dedication to physical filmmaking in an increasingly CGI-dominated landscape.
Beyond the thrills, "The Final Reckoning" also aims for a deeper emotional core. With its title hinting at a definitive conclusion, the film takes time to reflect on Ethan Hunt's journey over the past three decades. The interplay between Ethan and his long-standing team - the ever-loyal Luther (Ving Rhames) and Benji (Simon Pegg) - provides moments of warmth and camaraderie that ground the incredible events unfolding around them. The return of Henry Czerny as Kittridge is also a welcome addition, adding layers to the narrative.
While some critics have pointed to a slight overstuffed feeling in the plot or moments of exposition that can feel a touch heavy-handed, these are minor quibbles against the film's overwhelming strengths. The consensus is clear: "Mission: Impossible - The Final Reckoning" is a worthy, if potentially bittersweet, culmination of Ethan Hunt's incredible saga. It's a film that reminds us why we go to the movies - for the sheer escapism, the breathtaking spectacle, and the enduring power of a hero who always chooses to accept the impossible mission. If this truly is Ethan Hunt's final reckoning, he certainly goes out with a bang.
"""

result=model.invoke(Prompt)

print(result.content)
