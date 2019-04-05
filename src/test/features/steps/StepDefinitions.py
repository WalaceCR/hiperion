from behave import *
from src.test.util.Util import utilidades


@given(u'que o usuário acessa a página')
def step_impl(context):
    print("que o usuário acessa a página")
    utilidades.goto_page()


@given(u'a caixa de pesquisa existe')
def step_impl(context):
    print("a caixa de pesquisa existe")


@when(u'digito o conteúdo para pesquisa')
def step_impl(context):
    print("digito o conteúdo para pesquisa")


@when(u'clico no botão pesquisar')
def step_impl(context):
    print("clico no botão pesquisar")


@then(u'são exibidos os resultados da busca')
def step_impl(context):
    print("são exibidos os resultados da busca")

