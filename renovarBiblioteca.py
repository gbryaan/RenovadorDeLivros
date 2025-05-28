from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError; 


def renovarLivro(login, senha):


    with sync_playwright() as p:

        quantidadeLivros = 7;
        indiceLivro = 0;

        browser = p.firefox.launch();
        page = browser.new_page();
        page.goto("https://pergamum.ufam.edu.br/pergamum/biblioteca_s/meu_pergamum/index.php?flag=index.php");
        page.wait_for_load_state();
        page.locator('//*[@id="id_login"]').fill(login);
        page.locator('//*[@id="id_senhaLogin"]').fill(senha);
        page.locator('//*[@id="button"]').click();

        while(indiceLivro != -1):

            page.wait_for_load_state();
            indiceLivro += 1;
            
            try:
                xpath = f'//*[@id="botao_renovar{indiceLivro}"]'
                page.locator(xpath).click(timeout=5000);
                page.wait_for_load_state();
                page.locator('//*[@id="btn_gravar4"]').click();
            except PlaywrightTimeoutError:
                indiceLivro = -1;


        page.wait_for_load_state();
        page.close();



#Inicio da main

renovarLivro("suasenha", "seulogin");
