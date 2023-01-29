import os
import openai

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
        
def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)
        
        
openai.api_key = open_file('openaiapikey.txt')

def gpt3 (prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=1200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    text = response['choices'][0]['text'].strip()
    return text
    
ytopic = input("What is your Story About:\n\n")

#WRITE STORY
plot = open_file('prompt.txt').replace('<<PLOT>>', ytopic)
plot2 = gpt3(plot)
print('\n\nStory:', plot2)
save_file('story.txt', plot2)

#CREATE SCENES
storyinput = open_file('story.txt')
storys = open_file('prompt2.txt').replace('<<STORY>>', storyinput)
storys2 = gpt3(storys)
print('\n\nStoryscenes:', storys2)
save_file('story2.txt', storys2)

#MIDJOURNEY PROMPTS
mjprompt = open_file('mjprompts.txt')
mjprompt1 = open_file('prompt3.txt').replace('<<MJP>>', mjprompt).replace('<<SCENE>>', storys2)
mjprompt2 = gpt3(mjprompt1)
print('\n\nMJ-Prompts:', mjprompt2)
save_file('midjprompts.txt', mjprompt2)

#MIDJOURNEY + URL PROMPT
url = open_file('url.txt')
urlmj = open_file('prompt4.txt').replace('<<MJP>>', mjprompt2).replace('<<URL>>', url)
urlmj2 = gpt3(urlmj)
print('\n\nMJ-URL-Prompts:', urlmj2)
save_file('midjpromptsurl.txt', urlmj2)

#VOICEOVER
narrator = open_file('narrator.txt').replace('<<STORY>>', plot2)
narrator2 = gpt3(narrator)
print('\n\nVO Script:', narrator2)
save_file('voiceoverscript.txt', narrator2)