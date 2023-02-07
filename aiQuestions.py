# Copyright (c) 2023, Trent Kelly
# All rights reserved.

# This source code is licensed under the MIT-style license found in the
# LICENSE file in the root directory of this source tree. 

import config
import openai

def createQuestion(answer):
    # Load your API key from an environment variable or secret management service
    openai.api_key = config.config['OPENAI_API_KEY']

    #Get response from OpenAI
    response = openai.Completion.create(
        model="text-curie-001", 
        prompt="Make a test question to help remember this principle: " + answer, 
        temperature=1, 
        max_tokens=25)
    
    #Getting just question (text) instead of entire response
    question = response.choices[0].text
    return question