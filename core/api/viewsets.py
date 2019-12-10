from django.contrib.auth.models import User
from core.models import Log
from rest_framework import viewsets, status
from rest_framework.response import Response
from core.api.serializers import UserSerializer,LogSerializer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from core.api.conversation import conversation


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    def create(self, request):
      print(request.data['pergunta'])
      ask = request.data['pergunta']

      chatbot = ChatBot('Chatbot AnovaDS')

      trainer = ChatterBotCorpusTrainer(chatbot)

      trainer.train("chatterbot.corpus.portuguese.conversations")
      trainer.train("chatterbot.corpus.portuguese.greetings")
      trainer.train("chatterbot.corpus.portuguese.compliment")

      conv = conversation.frases()

      trainer = ListTrainer(chatbot)
      trainer.train(conv)
      resposta = chatbot.get_response(ask)

      if float(resposta.confidence > 0.5):
           #return Response({"resposta": resposta}, status=status.HTTP_200_OK)
            return Response('{{"Resposta":"{0}"}}'.format(resposta), status=status.HTTP_200_OK)
      else:
            print('Ron: Desculpe, eu não entendi o que você falou.')
        




      