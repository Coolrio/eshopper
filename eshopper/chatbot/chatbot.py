from chatterbot import ChatBot

chatbot = ChatBot(
    'mysqlbot',
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="mysql+pymysql://root:@localhost/eshopper",
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)


# Training With Corpus
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer_corpus = ChatterBotCorpusTrainer(chatbot)

trainer_corpus.train(
    'chatterbot.corpus.english'
)
