#!/usr/bin/env python3
"""Gera o site do MacMixer em inglês (raiz), português (/pt/) e espanhol (/es/).

Edite os textos aqui e rode `python3 build.py`; as páginas .html geradas são as que vão para o GitHub Pages.
Na raiz, um script leva o visitante para /pt/ ou /es/ conforme o idioma do navegador (ou a escolha feita
no seletor de idioma, guardada no navegador).
"""
import pathlib
from urllib.parse import quote

# Depois da primeira release (o release.sh põe MacMixer.dmg na raiz do site): True.
DOWNLOAD_READY = False
# Link de checkout do produto Live no Dodo (None enquanto não existir).
CHECKOUT_URL = None
# Print do painel em cada idioma (MacMixer --demo), mostrado logo abaixo do botão principal.
# Idioma sem print usa o de outro idioma.
SCREENSHOT = {"pt": "assets/screenshot-pt.png"}
SCREENSHOT_ALT = {"en": "MacMixer panel with a volume slider for each app and browser tab",
                  "pt": "Painel do MacMixer com um controle de volume para cada app e aba do navegador",
                  "es": "Panel de MacMixer con un control de volumen para cada app y pestaña del navegador"}

SITE = "https://macmixer-app.github.io"
EMAIL = "macmixer.app@gmail.com"
LANGS = {"en": "", "pt": "pt/", "es": "es/"}
HTML_LANG = {"en": "en", "pt": "pt-BR", "es": "es"}
PAGES = ["index", "terms", "privacy", "refund"]
ROOT = pathlib.Path(__file__).parent

UI = {
    "en": {
        "features": "Features", "pricing": "Pricing", "faq": "FAQ",
        "terms": "Terms", "privacy": "Privacy", "refunds": "Refunds",
        "updated": "Last updated: October 9, 2026",
        "note": "",
    },
    "pt": {
        "features": "Recursos", "pricing": "Preço", "faq": "Dúvidas",
        "terms": "Termos", "privacy": "Privacidade", "refunds": "Reembolso",
        "updated": "Atualizado em 9 de outubro de 2026",
        "note": "Esta tradução é para sua conveniência. Em caso de divergência, vale a "
                "<a href=\"../{page}.html\">versão em inglês</a>.",
    },
    "es": {
        "features": "Funciones", "pricing": "Precio", "faq": "Preguntas",
        "terms": "Términos", "privacy": "Privacidad", "refunds": "Reembolsos",
        "updated": "Última actualización: 9 de octubre de 2026",
        "note": "Esta traducción es para tu comodidad. En caso de discrepancia, prevalece la "
                "<a href=\"../{page}.html\">versión en inglés</a>.",
    },
}

INDEX = {
    "en": {
        "title": "MacMixer – Per-App & Browser Tab Volume Control for Mac",
        "description": "Set the volume of each app and each browser tab on your Mac, right from the menu bar, like the Windows volume mixer. Free 7-day trial, then $9.99 once.",
        "og_locale": "en_US",
        "eyebrow": "Menu bar app for macOS 15+",
        "h1": "A volume mixer for every app and browser tab on your Mac",
        "lead": "Turn down a loud YouTube tab without touching your Zoom call. MacMixer gives each app and each tab its own slider, right in the menu bar, like the Windows volume mixer.",
        "cta": "Try free for 7 days", "soon": "coming soon",
        "buy_link": "or buy now for $9.99",
        "microcopy": "Free 7-day trial · No account, no card · Then $9.99 once, no subscription",
        "badges": ["Notarized by Apple", "Audio stays on your Mac", "Apple Silicon & Intel", "14-day refund"],
        "mobile_text": "MacMixer runs on your Mac. Send yourself the link and try it there.",
        "mobile_button": "Send to my Mac",
        "share_title": "Try MacMixer on my Mac",
        "features_title": "Per-app and per-tab volume, right in the menu bar",
        "cards": [
            ("Volume per app", "A slider and a mute button for each app that is playing sound: music, calls, games, videos."),
            ("Volume per browser tab", "With the free browser extension, each tab in Chrome, Arc or Safari gets its own slider. Turn down a noisy tab without touching your call."),
            ("Remembers your levels", "Each app keeps the volume you chose the next time it plays. MacMixer opens with your Mac and stays in the menu bar."),
            ("Only touches what you change", "Apps you leave at 100% play exactly as before. The browser volume works as a ceiling for its tabs, and system sounds are tucked into their own section."),
        ],
        "steps_title": "Get started in 3 steps",
        "steps": [
            "Download MacMixer and drag it to your Applications folder.",
            "Open it and click the MacMixer icon in the menu bar.",
            "Move a slider. The first time, macOS asks for permission to capture audio: click Allow.",
        ],
        "safety_title": "Safe and private",
        "safety": [
            "macOS asks for permission to capture audio the first time you change a volume. That's how Apple lets one app adjust another app's sound: MacMixer processes it in real time on your Mac. Nothing is recorded, stored or sent.",
            "There's no audio driver or system extension to install, no account, no analytics and no ads. The app only goes online to check your license and look for updates.",
        ],
        "pricing_title": "Pricing",
        "amount": "$9.99", "once": "one-time",
        "tagline": "Pay once, use it forever.",
        "perks": ["Lifetime license, no subscription", "Use it on up to 2 Macs", "Includes updates to the current major version",
                  "Try everything free for 7 days first", "14-day money-back guarantee"],
        "buy": "Buy MacMixer – $9.99",
        "try_first": "Not sure yet? Try it free for 7 days",
        "mor": "Payments are processed by Dodo Payments, our Merchant of Record, which handles sales tax and VAT.",
        "faq_title": "FAQ",
        "faq": [
            ("Why does macOS ask for audio permission?", "To change an app's volume, MacMixer routes that app's sound through its own volume control, and macOS requires your permission for that. The sound is processed in real time on your Mac. Nothing is recorded, stored or sent anywhere."),
            ("Is MacMixer safe?", "Yes. It's signed and notarized by Apple, uses Apple's own audio APIs and installs no drivers or system extensions. There's no account, and your audio never leaves your Mac."),
            ("How does the free trial work?", "Download MacMixer and use every feature for 7 days, no payment details needed. When the trial ends, the app stops adjusting volumes and all sound goes back to normal until you activate a license."),
            ("How do I activate my license?", "After you buy, your license key arrives by email. Open MacMixer › Settings › License, paste the key and click Activate. You can deactivate it on one Mac to move it to another."),
            ("Do I need the browser extension?", "No. Without it, MacMixer controls each browser as a whole. With it, every tab gets its own slider. In Safari, the extension comes with the app; in Chrome and Arc, it takes about a minute to load in developer mode, with the steps in MacMixer › Settings."),
            ("How is it different from SoundSource?", "SoundSource is a powerful pro tool with effects, EQ, volume boost and per-app output devices. MacMixer does one thing: simple volume control for each app and each browser tab, for $9.99. If you need EQ and audio routing, SoundSource is excellent; if you just want to turn things down, MacMixer is lighter and cheaper."),
            ("There are free alternatives. Why pay?", "Some free tools are great. MacMixer adds per-tab volume for Chrome, Arc and Safari, works without installing a virtual audio driver, remembers each app's level and gets automatic updates. Try it free for 7 days and decide."),
            ("Does it work offline?", "Yes. MacMixer checks your license once a day when you're online, and keeps working for up to 30 days without a connection."),
            ("Which languages does it support?", "MacMixer is available in English, Portuguese and Spanish, and follows your Mac's language."),
            ("Can I get a refund?", "Yes, within 14 days of purchase. See the <a href=\"refund.html\">refund policy</a>."),
        ],
        "made_by": "Made by an independent developer in Brazil.",
    },
    "pt": {
        "title": "MacMixer – Volume por app e por aba do navegador no Mac",
        "description": "Ajuste o volume de cada app e de cada aba do navegador no seu Mac, direto da barra de menus, como o mixer de volume do Windows. 7 dias grátis, depois US$ 9,99 uma vez.",
        "og_locale": "pt_BR",
        "eyebrow": "App de barra de menus para macOS 15+",
        "h1": "Um mixer de volume para cada app e cada aba do seu Mac",
        "lead": "Abaixe aquela aba barulhenta do YouTube sem mexer na sua chamada do Zoom. O MacMixer dá a cada app e a cada aba o próprio controle, direto na barra de menus, como o mixer de volume do Windows.",
        "cta": "Testar grátis por 7 dias", "soon": "em breve",
        "buy_link": "ou compre agora por US$ 9,99",
        "microcopy": "7 dias grátis · Sem cadastro, sem cartão · Depois, US$ 9,99 uma vez, sem assinatura",
        "badges": ["Notarizado pela Apple", "O áudio não sai do seu Mac", "Apple Silicon e Intel", "Reembolso em 14 dias"],
        "mobile_text": "O MacMixer roda no Mac. Mande o link para você e teste lá.",
        "mobile_button": "Enviar para o meu Mac",
        "share_title": "Testar o MacMixer no meu Mac",
        "features_title": "Volume por app e por aba, direto na barra de menus",
        "cards": [
            ("Volume por app", "Um controle deslizante e um botão de mudo para cada app que está tocando som: música, chamadas, jogos, vídeos."),
            ("Volume por aba do navegador", "Com a extensão gratuita, cada aba do Chrome, Arc ou Safari ganha o próprio controle. Abaixe uma aba barulhenta sem mexer na sua chamada."),
            ("Lembra dos seus níveis", "Cada app volta com o volume que você escolheu na próxima vez que tocar. O MacMixer abre junto com o Mac e fica na barra de menus."),
            ("Só mexe no que você muda", "Apps que você deixa em 100% tocam exatamente como antes. O volume do navegador funciona como teto das abas, e os sons do sistema ficam numa seção separada."),
        ],
        "steps_title": "Comece em 3 passos",
        "steps": [
            "Baixe o MacMixer e arraste para a pasta Aplicativos.",
            "Abra o app e clique no ícone do MacMixer na barra de menus.",
            "Mexa num controle. Na primeira vez, o macOS pede permissão para capturar o áudio: clique em Permitir.",
        ],
        "safety_title": "Seguro e privado",
        "safety": [
            "O macOS pede permissão para capturar o áudio na primeira vez que você muda um volume. É assim que a Apple deixa um app ajustar o som de outro: o MacMixer processa o som em tempo real, no seu Mac. Nada é gravado, guardado ou enviado.",
            "Não há driver de áudio nem extensão de sistema para instalar, nem conta, estatísticas de uso ou anúncios. O app só acessa a internet para conferir sua licença e procurar atualizações.",
        ],
        "pricing_title": "Preço",
        "amount": "US$ 9,99", "once": "pagamento único",
        "tagline": "Pague uma vez, use para sempre.",
        "perks": ["Licença vitalícia, sem assinatura", "Use em até 2 Macs", "Inclui as atualizações da versão principal atual",
                  "Experimente tudo grátis por 7 dias antes", "Garantia de reembolso de 14 dias"],
        "buy": "Comprar o MacMixer – US$ 9,99",
        "try_first": "Ainda em dúvida? Teste grátis por 7 dias",
        "mor": "Os pagamentos são processados pelo Dodo Payments, nosso Merchant of Record, que cuida dos impostos sobre a venda.",
        "faq_title": "Dúvidas",
        "faq": [
            ("Por que o macOS pede permissão de áudio?", "Para mudar o volume de um app, o MacMixer passa o som desse app pelo próprio controle de volume, e o macOS exige a sua permissão para isso. O som é processado em tempo real no seu Mac. Nada é gravado, guardado ou enviado."),
            ("O MacMixer é seguro?", "Sim. Ele é assinado e notarizado pela Apple, usa as APIs de áudio da própria Apple e não instala drivers nem extensões de sistema. Não há conta, e o seu áudio nunca sai do Mac."),
            ("Como funciona o teste grátis?", "Baixe o MacMixer e use todos os recursos por 7 dias, sem cadastrar pagamento. Quando o teste acaba, o app para de ajustar os volumes e todo o som volta ao normal até você ativar uma licença."),
            ("Como ativo minha licença?", "Depois da compra, a chave de licença chega por e-mail. Abra MacMixer › Ajustes › Licença, cole a chave e clique em Ativar. Para levar a licença a outro Mac, desative-a no Mac atual."),
            ("Preciso da extensão do navegador?", "Não. Sem ela, o MacMixer controla cada navegador como um todo. Com ela, cada aba ganha o próprio controle. No Safari, a extensão vem com o app; no Chrome e no Arc, ela é carregada em cerca de um minuto pelo modo do desenvolvedor, com o passo a passo em MacMixer › Ajustes."),
            ("Qual a diferença para o SoundSource?", "O SoundSource é uma ferramenta profissional, com efeitos, equalizador, reforço de volume e saída de áudio por app. O MacMixer faz uma coisa só: controle de volume simples para cada app e cada aba do navegador, por US$ 9,99. Se você precisa de equalizador e roteamento de áudio, o SoundSource é excelente; se só quer abaixar o som das coisas, o MacMixer é mais leve e mais barato."),
            ("Existem alternativas grátis. Por que pagar?", "Algumas ferramentas grátis são ótimas. O MacMixer adiciona volume por aba no Chrome, Arc e Safari, funciona sem instalar um driver de áudio virtual, lembra o nível de cada app e recebe atualizações automáticas. Teste grátis por 7 dias e decida."),
            ("Funciona sem internet?", "Sim. O MacMixer confere a licença uma vez por dia quando está online e continua funcionando por até 30 dias sem conexão."),
            ("Em quais idiomas ele está?", "O MacMixer está em inglês, português e espanhol, e segue o idioma do seu Mac."),
            ("Posso pedir reembolso?", "Sim, em até 14 dias após a compra. Veja a <a href=\"refund.html\">política de reembolso</a>."),
        ],
        "made_by": "Feito por um desenvolvedor independente no Brasil.",
    },
    "es": {
        "title": "MacMixer – Volumen por app y por pestaña en tu Mac",
        "description": "Ajusta el volumen de cada app y de cada pestaña del navegador en tu Mac, desde la barra de menús, como el mezclador de volumen de Windows. 7 días gratis, después US$9.99 una vez.",
        "og_locale": "es_ES",
        "eyebrow": "App de la barra de menús para macOS 15+",
        "h1": "Un mezclador de volumen para cada app y cada pestaña de tu Mac",
        "lead": "Baja esa pestaña ruidosa de YouTube sin tocar tu llamada de Zoom. MacMixer le da a cada app y a cada pestaña su propio control, en la barra de menús, como el mezclador de volumen de Windows.",
        "cta": "Probar gratis 7 días", "soon": "próximamente",
        "buy_link": "o cómpralo ya por US$9.99",
        "microcopy": "7 días gratis · Sin cuenta ni tarjeta · Después, US$9.99 una sola vez, sin suscripción",
        "badges": ["Notarizado por Apple", "El audio no sale de tu Mac", "Apple Silicon e Intel", "Reembolso en 14 días"],
        "mobile_text": "MacMixer funciona en tu Mac. Envíate el enlace y pruébalo allí.",
        "mobile_button": "Enviar a mi Mac",
        "share_title": "Probar MacMixer en mi Mac",
        "features_title": "Volumen por app y por pestaña, en la barra de menús",
        "cards": [
            ("Volumen por app", "Un control deslizante y un botón de silencio para cada app que está reproduciendo sonido: música, llamadas, juegos, videos."),
            ("Volumen por pestaña", "Con la extensión gratuita, cada pestaña de Chrome, Arc o Safari tiene su propio control. Baja una pestaña ruidosa sin tocar tu llamada."),
            ("Recuerda tus niveles", "Cada app vuelve con el volumen que elegiste la próxima vez que suene. MacMixer se abre con tu Mac y se queda en la barra de menús."),
            ("Solo toca lo que cambias", "Las apps que dejas al 100% suenan exactamente igual que antes. El volumen del navegador funciona como tope de sus pestañas, y los sonidos del sistema quedan en su propia sección."),
        ],
        "steps_title": "Empieza en 3 pasos",
        "steps": [
            "Descarga MacMixer y arrástralo a la carpeta Aplicaciones.",
            "Ábrelo y haz clic en el icono de MacMixer en la barra de menús.",
            "Mueve un control. La primera vez, macOS pide permiso para capturar el audio: haz clic en Permitir.",
        ],
        "safety_title": "Seguro y privado",
        "safety": [
            "macOS pide permiso para capturar el audio la primera vez que cambias un volumen. Así es como Apple permite que una app ajuste el sonido de otra: MacMixer lo procesa en tiempo real, en tu Mac. No se graba, guarda ni envía nada.",
            "No hay driver de audio ni extensión del sistema que instalar, ni cuenta, estadísticas de uso o anuncios. La app solo se conecta a internet para verificar tu licencia y buscar actualizaciones.",
        ],
        "pricing_title": "Precio",
        "amount": "US$9.99", "once": "pago único",
        "tagline": "Paga una vez, úsalo para siempre.",
        "perks": ["Licencia de por vida, sin suscripción", "Úsala en hasta 2 Macs", "Incluye las actualizaciones de la versión principal actual",
                  "Prueba todo gratis durante 7 días", "Garantía de reembolso de 14 días"],
        "buy": "Comprar MacMixer – US$9.99",
        "try_first": "¿Aún no lo tienes claro? Pruébalo gratis 7 días",
        "mor": "Los pagos los procesa Dodo Payments, nuestro Merchant of Record, que se encarga de los impuestos sobre las ventas.",
        "faq_title": "Preguntas frecuentes",
        "faq": [
            ("¿Por qué macOS pide permiso de audio?", "Para cambiar el volumen de una app, MacMixer pasa el sonido de esa app por su propio control de volumen, y macOS exige tu permiso para eso. El sonido se procesa en tiempo real en tu Mac. No se graba, guarda ni envía nada."),
            ("¿Es seguro MacMixer?", "Sí. Está firmado y notarizado por Apple, usa las APIs de audio de la propia Apple y no instala drivers ni extensiones del sistema. No hay cuenta, y tu audio nunca sale de tu Mac."),
            ("¿Cómo funciona la prueba gratis?", "Descarga MacMixer y usa todas las funciones durante 7 días, sin datos de pago. Cuando la prueba termina, la app deja de ajustar los volúmenes y todo el sonido vuelve a la normalidad hasta que actives una licencia."),
            ("¿Cómo activo mi licencia?", "Después de comprar, la clave de licencia te llega por correo. Abre MacMixer › Ajustes › Licencia, pega la clave y haz clic en Activar. Para pasarla a otro Mac, desactívala en el Mac actual."),
            ("¿Necesito la extensión del navegador?", "No. Sin ella, MacMixer controla cada navegador completo. Con ella, cada pestaña tiene su propio control. En Safari, la extensión viene con la app; en Chrome y Arc, se carga en un minuto con el modo de desarrollador, con los pasos en MacMixer › Ajustes."),
            ("¿En qué se diferencia de SoundSource?", "SoundSource es una herramienta profesional con efectos, ecualizador, refuerzo de volumen y salida de audio por app. MacMixer hace una sola cosa: control de volumen simple para cada app y cada pestaña del navegador, por US$9.99. Si necesitas ecualizador y enrutamiento de audio, SoundSource es excelente; si solo quieres bajar el sonido de las cosas, MacMixer es más ligero y más barato."),
            ("Hay alternativas gratis. ¿Por qué pagar?", "Algunas herramientas gratis son muy buenas. MacMixer añade volumen por pestaña en Chrome, Arc y Safari, funciona sin instalar un driver de audio virtual, recuerda el nivel de cada app y recibe actualizaciones automáticas. Pruébalo gratis 7 días y decide."),
            ("¿Funciona sin conexión?", "Sí. MacMixer verifica tu licencia una vez al día cuando estás en línea y sigue funcionando hasta 30 días sin conexión."),
            ("¿En qué idiomas está?", "MacMixer está en inglés, portugués y español, y sigue el idioma de tu Mac."),
            ("¿Puedo pedir un reembolso?", "Sí, dentro de los 14 días posteriores a la compra. Consulta la <a href=\"refund.html\">política de reembolso</a>."),
        ],
        "made_by": "Hecho por un desarrollador independiente en Brasil.",
    },
}

DOCS = {
    "privacy": {
        "en": ("Privacy Policy", [
            (None, "MacMixer is a macOS app that adjusts the volume of apps and browser tabs on your Mac. It is built to collect as little as possible: there are no accounts, no analytics, no tracking and no ads."),
            ("Audio", "To change an app's volume, MacMixer routes that app's sound through its own volume control on your Mac. This requires the macOS Audio Recording permission. The audio is processed in real time on your Mac and is never recorded, stored or sent anywhere."),
            ("Browser extension", "The optional extension sends the title, address and icon address of tabs that are playing sound to the MacMixer app, so it can show them in the mixer. This information only travels between your browser and the app on your own computer (through a local connection on 127.0.0.1) and is not sent to us or anyone else."),
            (None, "To show a tab's icon, the app may download that site's icon (favicon) directly from the website, as your browser does."),
            ("License checks", "When you activate a license, MacMixer sends your license key and your Mac's name to Dodo Payments, our payment and licensing provider, so the activation can be listed under your license. Once a day, while you're online, the app sends the license key and activation ID to confirm the license is still valid. The provider receives your IP address as part of any internet request."),
            ("Updates", "MacMixer checks for updates by downloading a public update list from this website, hosted on GitHub Pages. The request doesn't include any information about you or your Mac beyond what any web request includes (such as your IP address). You can turn automatic checks off in MacMixer › Settings."),
            ("Purchases", "Purchases are processed by Dodo Payments, which acts as Merchant of Record and collects the information needed to process your payment, deliver your license key and comply with tax rules. We receive your name, email address and order details so we can provide support. We don't receive or store your card details. See the <a href=\"https://dodopayments.com/privacy-policy\">Dodo Payments privacy policy</a>."),
            ("Data on your Mac", "Your volume settings are stored in the app's preferences on your Mac. Your license key and the trial start date are stored in your macOS Keychain. Deleting the app's preferences and Keychain items removes them."),
            ("Contact", f"Questions or requests about your data: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>."),
        ]),
        "pt": ("Política de Privacidade", [
            (None, "O MacMixer é um app para macOS que ajusta o volume de apps e de abas do navegador no seu Mac. Ele foi feito para coletar o mínimo possível: sem contas, sem estatísticas de uso, sem rastreamento e sem anúncios."),
            ("Áudio", "Para mudar o volume de um app, o MacMixer passa o som desse app pelo próprio controle de volume, no seu Mac. Isso exige a permissão de Gravação de Áudio do macOS. O áudio é processado em tempo real no seu Mac e nunca é gravado, guardado ou enviado a lugar nenhum."),
            ("Extensão do navegador", "A extensão opcional envia ao app MacMixer o título, o endereço e o endereço do ícone das abas que estão tocando som, para mostrá-las no mixer. Essas informações só circulam entre o seu navegador e o app no seu próprio computador (por uma conexão local em 127.0.0.1) e não são enviadas para nós nem para mais ninguém."),
            (None, "Para mostrar o ícone de uma aba, o app pode baixar o ícone (favicon) direto do site, como o seu navegador faz."),
            ("Verificação da licença", "Ao ativar uma licença, o MacMixer envia a chave e o nome do seu Mac ao Dodo Payments, nosso provedor de pagamentos e licenças, para a ativação aparecer na sua licença. Uma vez por dia, quando há internet, o app envia a chave e o ID da ativação para confirmar que a licença continua válida. O provedor recebe o seu endereço IP, como em qualquer acesso à internet."),
            ("Atualizações", "O MacMixer procura atualizações baixando uma lista pública de versões deste site, hospedado no GitHub Pages. O pedido não inclui nenhuma informação sobre você ou o seu Mac além do que qualquer acesso à internet inclui (como o seu endereço IP). Você pode desligar a verificação automática em MacMixer › Ajustes."),
            ("Compras", "As compras são processadas pelo Dodo Payments, que atua como Merchant of Record e coleta as informações necessárias para processar o pagamento, entregar a chave de licença e cumprir as regras fiscais. Recebemos seu nome, e-mail e os dados do pedido para poder dar suporte. Não recebemos nem guardamos os dados do seu cartão. Veja a <a href=\"https://dodopayments.com/privacy-policy\">política de privacidade do Dodo Payments</a>."),
            ("Dados no seu Mac", "Seus ajustes de volume ficam nas preferências do app, no seu Mac. A chave de licença e a data de início do teste ficam nas Chaves (Keychain) do macOS. Apagar as preferências do app e esses itens das Chaves remove tudo."),
            ("Contato", f"Dúvidas ou pedidos sobre os seus dados: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>."),
        ]),
        "es": ("Política de Privacidad", [
            (None, "MacMixer es una app para macOS que ajusta el volumen de apps y pestañas del navegador en tu Mac. Está hecha para recopilar lo mínimo posible: sin cuentas, sin estadísticas de uso, sin rastreo y sin anuncios."),
            ("Audio", "Para cambiar el volumen de una app, MacMixer pasa el sonido de esa app por su propio control de volumen, en tu Mac. Esto requiere el permiso de Grabación de audio de macOS. El audio se procesa en tiempo real en tu Mac y nunca se graba, guarda ni envía a ningún lugar."),
            ("Extensión del navegador", "La extensión opcional envía a la app MacMixer el título, la dirección y la dirección del icono de las pestañas que están reproduciendo sonido, para mostrarlas en el mezclador. Esta información solo viaja entre tu navegador y la app en tu propio ordenador (por una conexión local en 127.0.0.1) y no se envía a nosotros ni a nadie más."),
            (None, "Para mostrar el icono de una pestaña, la app puede descargar el icono (favicon) directamente del sitio web, como hace tu navegador."),
            ("Verificación de la licencia", "Al activar una licencia, MacMixer envía tu clave y el nombre de tu Mac a Dodo Payments, nuestro proveedor de pagos y licencias, para que la activación aparezca en tu licencia. Una vez al día, cuando hay conexión, la app envía la clave y el ID de la activación para confirmar que la licencia sigue siendo válida. El proveedor recibe tu dirección IP, como en cualquier acceso a internet."),
            ("Actualizaciones", "MacMixer busca actualizaciones descargando una lista pública de versiones de este sitio, alojado en GitHub Pages. La solicitud no incluye ninguna información sobre ti o tu Mac más allá de lo que incluye cualquier acceso a internet (como tu dirección IP). Puedes desactivar la búsqueda automática en MacMixer › Ajustes."),
            ("Compras", "Las compras las procesa Dodo Payments, que actúa como Merchant of Record y recopila la información necesaria para procesar el pago, entregar la clave de licencia y cumplir las normas fiscales. Recibimos tu nombre, correo y los datos del pedido para poder darte soporte. No recibimos ni guardamos los datos de tu tarjeta. Consulta la <a href=\"https://dodopayments.com/privacy-policy\">política de privacidad de Dodo Payments</a>."),
            ("Datos en tu Mac", "Tus ajustes de volumen se guardan en las preferencias de la app, en tu Mac. La clave de licencia y la fecha de inicio de la prueba se guardan en el Llavero de macOS. Borrar las preferencias de la app y esos elementos del Llavero lo elimina todo."),
            ("Contacto", f"Preguntas o solicitudes sobre tus datos: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>."),
        ]),
    },
    "terms": {
        "en": ("Terms of Use", [
            (None, "These terms apply to your use of the MacMixer app and license. By downloading, installing or buying MacMixer, you agree to them."),
            ("Trial and license", "You can use every feature of MacMixer free for 7 days. After that, a license is needed to keep adjusting volumes. A license is a one-time purchase that lets one person use MacMixer on up to 2 Macs they own or control, and includes updates for the current major version. Future major versions may be offered as a paid upgrade."),
            (None, "The license is personal and may not be shared, resold or published. We may deactivate license keys that are shared publicly, refunded, or obtained through fraud or chargebacks."),
            ("Purchases", "Orders are processed by Dodo Payments, our Merchant of Record, which is the seller for the transaction and handles payment, taxes and invoicing. Prices are shown in US dollars; applicable taxes are added at checkout. Refunds follow our <a href=\"refund.html\">refund policy</a>."),
            ("Acceptable use", "You may not reverse engineer the licensing, remove license checks, or redistribute the app. You're responsible for using MacMixer in compliance with the laws that apply to you, including laws about recording or modifying audio."),
            ("No warranty", "MacMixer is provided \"as is\". We work to keep it reliable, but we don't guarantee it will work with every app, browser, audio device or macOS version, or that it will be free of errors. If MacMixer can't safely control an app's audio, it lets the original sound play normally."),
            ("Limitation of liability", "To the extent permitted by law, our total liability for any claim related to MacMixer is limited to the amount you paid for your license."),
            ("Changes", "We may update these terms. The date at the top shows the latest version. Continuing to use MacMixer after a change means you accept the new terms."),
            ("Contact", f"<a href=\"mailto:{EMAIL}\">{EMAIL}</a>"),
        ]),
        "pt": ("Termos de Uso", [
            (None, "Estes termos valem para o uso do app MacMixer e da licença. Ao baixar, instalar ou comprar o MacMixer, você concorda com eles."),
            ("Teste e licença", "Você pode usar todos os recursos do MacMixer de graça por 7 dias. Depois disso, é preciso uma licença para continuar ajustando os volumes. A licença é uma compra única que permite a uma pessoa usar o MacMixer em até 2 Macs que ela possua ou controle, e inclui as atualizações da versão principal atual. Versões principais futuras podem ser oferecidas como upgrade pago."),
            (None, "A licença é pessoal e não pode ser compartilhada, revendida ou publicada. Podemos desativar chaves de licença compartilhadas publicamente, reembolsadas ou obtidas por fraude ou contestação de pagamento."),
            ("Compras", "Os pedidos são processados pelo Dodo Payments, nosso Merchant of Record, que é o vendedor da transação e cuida do pagamento, dos impostos e da nota fiscal. Os preços são mostrados em dólares americanos; os impostos aplicáveis são somados no checkout. Os reembolsos seguem a nossa <a href=\"refund.html\">política de reembolso</a>."),
            ("Uso aceitável", "Você não pode fazer engenharia reversa do licenciamento, remover as verificações de licença nem redistribuir o app. Você é responsável por usar o MacMixer de acordo com as leis que se aplicam a você, inclusive as leis sobre gravar ou modificar áudio."),
            ("Sem garantia", "O MacMixer é fornecido \"no estado em que se encontra\". Trabalhamos para que ele seja confiável, mas não garantimos que funcione com todo app, navegador, dispositivo de áudio ou versão do macOS, nem que seja livre de erros. Se o MacMixer não conseguir controlar o áudio de um app com segurança, ele deixa o som original tocar normalmente."),
            ("Limitação de responsabilidade", "Na medida permitida por lei, nossa responsabilidade total por qualquer reclamação relacionada ao MacMixer é limitada ao valor que você pagou pela licença."),
            ("Mudanças", "Podemos atualizar estes termos. A data no topo indica a versão mais recente. Continuar usando o MacMixer depois de uma mudança significa que você aceita os novos termos."),
            ("Contato", f"<a href=\"mailto:{EMAIL}\">{EMAIL}</a>"),
        ]),
        "es": ("Términos de Uso", [
            (None, "Estos términos se aplican al uso de la app MacMixer y de su licencia. Al descargar, instalar o comprar MacMixer, los aceptas."),
            ("Prueba y licencia", "Puedes usar todas las funciones de MacMixer gratis durante 7 días. Después, necesitas una licencia para seguir ajustando los volúmenes. La licencia es una compra única que permite a una persona usar MacMixer en hasta 2 Macs de su propiedad o bajo su control, e incluye las actualizaciones de la versión principal actual. Las versiones principales futuras pueden ofrecerse como actualización de pago."),
            (None, "La licencia es personal y no se puede compartir, revender ni publicar. Podemos desactivar claves de licencia compartidas públicamente, reembolsadas u obtenidas mediante fraude o contracargos."),
            ("Compras", "Los pedidos los procesa Dodo Payments, nuestro Merchant of Record, que es el vendedor de la transacción y se encarga del pago, los impuestos y la facturación. Los precios se muestran en dólares estadounidenses; los impuestos aplicables se suman en el pago. Los reembolsos siguen nuestra <a href=\"refund.html\">política de reembolso</a>."),
            ("Uso aceptable", "No puedes aplicar ingeniería inversa al sistema de licencias, quitar las verificaciones de licencia ni redistribuir la app. Eres responsable de usar MacMixer de acuerdo con las leyes que te correspondan, incluidas las leyes sobre grabar o modificar audio."),
            ("Sin garantía", "MacMixer se ofrece \"tal cual\". Trabajamos para que sea fiable, pero no garantizamos que funcione con todas las apps, navegadores, dispositivos de audio o versiones de macOS, ni que esté libre de errores. Si MacMixer no puede controlar el audio de una app de forma segura, deja que el sonido original suene normalmente."),
            ("Limitación de responsabilidad", "En la medida en que lo permita la ley, nuestra responsabilidad total por cualquier reclamación relacionada con MacMixer se limita al importe que pagaste por tu licencia."),
            ("Cambios", "Podemos actualizar estos términos. La fecha en la parte superior indica la versión más reciente. Seguir usando MacMixer después de un cambio significa que aceptas los nuevos términos."),
            ("Contacto", f"<a href=\"mailto:{EMAIL}\">{EMAIL}</a>"),
        ]),
    },
    "refund": {
        "en": ("Refund Policy", [
            (None, "We want you to be happy with MacMixer. That's why there's a free 7-day trial with every feature, so you can make sure it works with your Mac, apps and audio devices before buying."),
            ("14-day money-back guarantee", f"If MacMixer doesn't work for you, ask for a full refund within 14 days of purchase. Email <a href=\"mailto:{EMAIL}\">{EMAIL}</a> with the email address used for the purchase, or reply to your receipt. No long explanations needed, though we'd love to know what went wrong so we can fix it."),
            ("How refunds are processed", "Refunds are issued by Dodo Payments, our Merchant of Record, to the original payment method. Depending on your bank, it may take 5 to 10 business days to appear. When a purchase is refunded, its license key is deactivated."),
            ("After 14 days", "After 14 days, refunds are at our discretion. If something is broken, get in touch anyway and we'll do our best to help."),
        ]),
        "pt": ("Política de Reembolso", [
            (None, "Queremos que você fique satisfeito com o MacMixer. Por isso há um teste grátis de 7 dias com todos os recursos, para você conferir se ele funciona com o seu Mac, seus apps e seus dispositivos de áudio antes de comprar."),
            ("Garantia de reembolso de 14 dias", f"Se o MacMixer não funcionar para você, peça o reembolso integral em até 14 dias após a compra. Escreva para <a href=\"mailto:{EMAIL}\">{EMAIL}</a> com o e-mail usado na compra, ou responda ao recibo. Não precisa de longas explicações, mas adoraríamos saber o que deu errado para corrigir."),
            ("Como o reembolso é feito", "O reembolso é feito pelo Dodo Payments, nosso Merchant of Record, para o mesmo meio de pagamento. Dependendo do seu banco, pode levar de 5 a 10 dias úteis para aparecer. Quando uma compra é reembolsada, a chave de licença é desativada."),
            ("Depois de 14 dias", "Depois de 14 dias, o reembolso fica a nosso critério. Se algo não estiver funcionando, entre em contato mesmo assim e faremos o possível para ajudar."),
        ]),
        "es": ("Política de Reembolso", [
            (None, "Queremos que estés contento con MacMixer. Por eso hay una prueba gratis de 7 días con todas las funciones, para que compruebes que funciona con tu Mac, tus apps y tus dispositivos de audio antes de comprar."),
            ("Garantía de reembolso de 14 días", f"Si MacMixer no te funciona, pide el reembolso completo dentro de los 14 días posteriores a la compra. Escribe a <a href=\"mailto:{EMAIL}\">{EMAIL}</a> con el correo que usaste en la compra, o responde al recibo. No hacen falta largas explicaciones, aunque nos encantaría saber qué falló para corregirlo."),
            ("Cómo se hace el reembolso", "El reembolso lo realiza Dodo Payments, nuestro Merchant of Record, al mismo medio de pago. Según tu banco, puede tardar de 5 a 10 días hábiles en aparecer. Cuando se reembolsa una compra, su clave de licencia se desactiva."),
            ("Después de 14 días", "Después de 14 días, el reembolso queda a nuestra discreción. Si algo no funciona, escríbenos de todos modos y haremos lo posible por ayudarte."),
        ]),
    },
}

REDIRECT = """<script>
    // Primeira visita: leva para o idioma do navegador; depois, vale o que a pessoa escolheu no seletor.
    (function () {
      var lang = null;
      try { lang = localStorage.getItem("lang"); } catch (e) {}
      if (!lang) {
        var preferred = ((navigator.languages && navigator.languages[0]) || navigator.language || "").toLowerCase();
        lang = preferred.indexOf("pt") === 0 ? "pt" : preferred.indexOf("es") === 0 ? "es" : "en";
      }
      if (lang === "pt" || lang === "es") {
        location.replace("/" + lang + "/" + location.pathname.split("/").pop() + location.hash);
      }
    })();
  </script>"""

REMEMBER = """<script>
    document.querySelectorAll("nav.lang a").forEach(function (link) {
      link.addEventListener("click", function () {
        try { localStorage.setItem("lang", link.dataset.lang); } catch (e) {}
      });
    });
  </script>"""


def url(lang, page, root):
    """Link relativo para `page` no idioma `lang`, a partir de uma página cuja raiz é `root`."""
    return root + LANGS[lang] + ("" if page == "index" else f"{page}.html") or "./"


def layout(lang, page, title, description, body, extra_head=""):
    root = "" if lang == "en" else "../"
    ui = UI[lang]
    alternates = "\n".join(
        f'  <link rel="alternate" hreflang="{HTML_LANG[l]}" href="{SITE}/{LANGS[l]}{"" if page == "index" else page + ".html"}">'
        for l in LANGS)
    current = ' aria-current="true"'
    switcher = "".join(
        f'<a href="{url(l, page, root)}" data-lang="{l}" hreflang="{HTML_LANG[l]}"'
        f'{current if l == lang else ""}>{l.upper()}</a>' for l in LANGS)
    sections = (f'<a href="#features">{ui["features"]}</a><a href="#pricing">{ui["pricing"]}</a><a href="#faq">{ui["faq"]}</a>'
                if page == "index" else
                f'<a href="{url(lang, "index", root)}#pricing">{ui["pricing"]}</a><a href="{url(lang, "index", root)}#faq">{ui["faq"]}</a>')
    path = "" if page == "index" else f"{page}.html"
    canonical = f"{SITE}/{LANGS[lang]}{path}"
    og_locale = INDEX[lang]["og_locale"]
    description_tag = f"""
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="MacMixer">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}/assets/og-{lang}.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="{og_locale}">
  <meta name="twitter:card" content="summary_large_image">"""
    return f"""<!doctype html>
<html lang="{HTML_LANG[lang]}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>{description_tag}
{alternates}
  <link rel="alternate" hreflang="x-default" href="{SITE}/{"" if page == "index" else page + ".html"}">
  <link rel="icon" type="image/png" sizes="32x32" href="{root}assets/favicon-32.png">
  <link rel="icon" type="image/png" sizes="64x64" href="{root}assets/favicon-64.png">
  <link rel="apple-touch-icon" href="{root}assets/icon-512.png">
  <link rel="stylesheet" href="{root}assets/style.css">
  {REDIRECT if lang == "en" else ""}{extra_head}
</head>
<body>
  <div class="wrap">
    <header class="top">
      <a class="brand" href="{url(lang, "index", root)}"><img src="{root}assets/favicon-64.png" alt="">MacMixer</a>
      <div class="right">
        <nav class="sections">{sections}</nav>
        <nav class="lang" aria-label="Language">{switcher}</nav>
      </div>
    </header>
{body}
    <footer>
      <span>© 2026 MacMixer · {INDEX[lang]["made_by"]} · <a href="mailto:{EMAIL}">{EMAIL}</a></span>
      <nav>
        <a href="terms.html">{ui["terms"]}</a>
        <a href="privacy.html">{ui["privacy"]}</a>
        <a href="refund.html">{ui["refunds"]}</a>
      </nav>
    </footer>
  </div>
  {REMEMBER}
</body>
</html>
"""


def index(lang):
    t = INDEX[lang]
    root = "" if lang == "en" else "../"
    if DOWNLOAD_READY:
        download = f'<a class="button primary large" href="{root}MacMixer.dmg">{t["cta"]}</a>'
    else:
        download = f'<a class="button primary large disabled" href="{root}MacMixer.dmg" aria-disabled="true">{t["cta"]} — {t["soon"]}</a>'
    buy_href = CHECKOUT_URL or "#pricing"
    if CHECKOUT_URL:
        buy = f'<a class="button primary" href="{CHECKOUT_URL}">{t["buy"]}</a>'
    else:
        buy = f'<a class="button primary disabled" href="#" aria-disabled="true">{t["buy"]} — {t["soon"]}</a>'
    badges = "".join(f"<li>{b}</li>" for b in t["badges"])
    shot = SCREENSHOT.get(lang) or next(iter(SCREENSHOT.values()), None)
    screenshot = ""
    if shot:
        header = pathlib.Path(shot).read_bytes()[16:24]  # largura e altura no cabeçalho do PNG
        width, height = int.from_bytes(header[:4], "big"), int.from_bytes(header[4:], "big")
        screenshot = f'\n      <img class="screenshot" src="{root}{shot}" alt="{SCREENSHOT_ALT[lang]}" width="{width}" height="{height}">'
    cards = "\n".join(f'        <div class="card">\n          <h3>{h}</h3>\n          <p>{p}</p>\n        </div>' for h, p in t["cards"])
    steps = "\n".join(f"        <li>{step}</li>" for step in t["steps"])
    safety = "\n".join(f"      <p>{p}</p>" for p in t["safety"])
    perks = "\n".join(f"          <li>{p}</li>" for p in t["perks"])
    faq = "\n".join(f"      <details>\n        <summary>{q}</summary>\n        <p>{a}</p>\n      </details>" for q, a in t["faq"])
    share_url = f"{SITE}/{LANGS[lang]}?ref=mobile"
    body = f"""
    <div class="hero" id="top">
      <img class="hero-icon" src="{root}assets/icon-512.png" alt="">
      <p class="eyebrow">{t["eyebrow"]}</p>
      <h1>{t["h1"]}</h1>
      <p class="lead">{t["lead"]}</p>
      <div class="actions desktop-only">
        {download}
      </div>
      <p class="buy-link desktop-only"><a href="{buy_href}">{t["buy_link"]}</a></p>
      <div class="mobile-only">
        <p class="mobile-text">{t["mobile_text"]}</p>
        <a class="button primary large" id="send-to-mac" href="mailto:?subject={quote(t["share_title"])}&amp;body={quote(share_url, safe="")}">{t["mobile_button"]}</a>
      </div>
      <p class="microcopy">{t["microcopy"]}</p>
      <ul class="badges">{badges}</ul>{screenshot}
    </div>

    <section id="features">
      <h2>{t["features_title"]}</h2>
      <div class="grid">
{cards}
      </div>
    </section>

    <section id="start">
      <h2>{t["steps_title"]}</h2>
      <ol class="steps">
{steps}
      </ol>
    </section>

    <section id="privacy">
      <h2>{t["safety_title"]}</h2>
{safety}
    </section>

    <section id="pricing">
      <h2>{t["pricing_title"]}</h2>
      <div class="price">
        <div class="amount">{t["amount"]} <small>{t["once"]}</small></div>
        <p class="tagline">{t["tagline"]}</p>
        <ul>
{perks}
        </ul>
        {buy}
        <p class="try-first"><a href="#top">{t["try_first"]}</a></p>
      </div>
      <p class="note">{t["mor"]}</p>
    </section>

    <section id="faq">
      <h2>{t["faq_title"]}</h2>
{faq}
    </section>
"""
    extra_head = f"""
  <script type="application/ld+json">{{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "MacMixer",
    "operatingSystem": "macOS 15 or later", "applicationCategory": "UtilitiesApplication", "inLanguage": "{HTML_LANG[lang]}",
    "description": "{t["description"]}", "url": "{SITE}/{LANGS[lang]}",
    "offers": {{"@type": "Offer", "price": "9.99", "priceCurrency": "USD"}}}}</script>
  <script>
    // Celular ou iPad não instalam o app: o botão principal vira "enviar para o meu Mac".
    if (/iPhone|iPod|Android/i.test(navigator.userAgent) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1)) {{
      document.documentElement.classList.add("is-mobile");
    }}
    document.addEventListener("DOMContentLoaded", function () {{
      var send = document.getElementById("send-to-mac");
      if (send && navigator.share) {{
        send.addEventListener("click", function (event) {{
          event.preventDefault();
          navigator.share({{ title: "{t["share_title"]}", url: "{share_url}" }}).catch(function () {{}});
        }});
      }}
    }});
  </script>"""
    return layout(lang, "index", t["title"], t["description"], body, extra_head)


def doc(lang, page):
    title, blocks = DOCS[page][lang]
    note = UI[lang]["note"].format(page=page)
    parts = [f'    <main class="doc">\n      <h1>{title}</h1>\n      <p class="updated">{UI[lang]["updated"]}</p>']
    if note:
        parts.append(f'      <p class="translation-note">{note}</p>')
    for heading, text in blocks:
        if heading:
            parts.append(f"\n      <h2>{heading}</h2>")
        parts.append(f"      <p>{text}</p>")
    parts.append("    </main>")
    description = f"{title} · MacMixer: {INDEX[lang]['eyebrow']}"
    return layout(lang, page, f"{title} · MacMixer", description, "\n".join(parts))


for lang, folder in LANGS.items():
    (ROOT / folder).mkdir(exist_ok=True)
    for page in PAGES:
        html = index(lang) if page == "index" else doc(lang, page)
        (ROOT / folder / f"{page}.html").write_text(html)
print("OK:", ", ".join(f"/{folder}" for folder in LANGS.values()))
