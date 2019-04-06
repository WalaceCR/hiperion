from behave import *
from src.test.util.Util import utilidades
from src.test.pageobject.PaginaInicial import PaginaInicial

@given(u'que o usuário acessa a página')
def step_impl(context):
    print("que o usuário acessa a página")
    utilidades.goto_page()


@when(u'digito o conteúdo para pesquisa')
def step_impl(context):
    print("digito o conteúdo para pesquisa")
    context.pagina_pesquisa = PaginaInicial(utilidades.get_driver())
    context.pagina_pesquisa.digitar_pesquisa()


@when(u'clico no botão pesquisar')
def step_impl(context):
    print("clico no botão pesquisar")
    context.pagina_pesquisa.clicar_em_pesquisa()


@then(u'são exibidos os resultados da busca')
def step_impl(context):
    print("são exibidos os resultados da busca")

