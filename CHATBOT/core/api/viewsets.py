from django.contrib.auth.models import User
from core.models import Log
from rest_framework import viewsets, status, parsers
from rest_framework.response import Response
from core.api.serializers import UserSerializer, LogSerializer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from core.api.conversation import conversation
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    parser_classes = (parsers.JSONParser,)

    def create(self, request):
        print(request.data['pergunta'])
        ask = request.data['pergunta']

        chatbot = ChatBot('Chatbot AnovaDS')

        trainer = ChatterBotCorpusTrainer(chatbot)

        # trainer.train("chatterbot.corpus.portuguese.conversations")
        # trainer.train("chatterbot.corpus.portuguese.greetings")
        # trainer.train("chatterbot.corpus.portuguese.compliment")

        conv = conversation.frases()

        trainer = ListTrainer(chatbot)
        trainer.train(conv)
        resposta = chatbot.get_response(ask)
        str(resposta)
        if float(resposta.confidence > 0.5):
            # serializer = self.get_serializer(resposta)
            # return Response(serializer.data)
            return Response(("resposta:""{0}").format(resposta), status=status.HTTP_200_OK, content_type="application/json")

            # return Response(status=status.HTTP_200_OK)
            # return Response(str(resposta), status=status.HTTP_200_OK)
        else:
            print('Desculpe, eu não entendi o que você falou.')
