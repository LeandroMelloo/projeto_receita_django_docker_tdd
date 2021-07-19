from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

data = [
    {
        "id": 1,
        "nome": "Leandro Mello",
        "descricao": "Faculdade Uniban",
        "status": "Ativo",
        "criado": "01/07/2021 - 12:39",
        "acoes": "deletar"
    },
    {
        "id": 2,
        "nome": "Luciana Mello",
        "descricao": "Faculdade Cruzeiro do Sul",
        "status": "Ativo",
        "criado": "01/07/2021 - 12:39",
        "acoes": "editar"
    }
]


class ReportAPIView(APIView):
    """API de Reports"""

    def get(self, request):
        return Response(data, status=status.HTTP_200_OK)
