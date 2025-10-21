*** Settings ***
Documentation     Teste de login no sistema Flask
Library           SeleniumLibrary
Resource          ../resources/variables.resource

*** Test Cases ***
Login Bem-Sucedido Como Admin
    [Documentation]    Verifica se o admin consegue logar e ver a mensagem de sucesso
    Open Browser    ${BASE_URL}/login    ${BROWSER}
    Input Text      name:username        ${ADMIN_USER}
    Input Password  name:password        ${ADMIN_PASS}
    Click Button    Entrar
    Page Should Contain    Olá, admin! Papel: ADMIN.
    Close Browser
