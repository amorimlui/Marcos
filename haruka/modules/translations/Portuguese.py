RUN_STRINGS = (
    "Onde você acha que vai?",
    "An? O que? Foi embora?",
    "ZzzzzZZZzz… O que foi? Como? Ah, isso outra vez, não importa",
    "Volta aqui!",
    "Não tão rápido...",
    "Cuidado com a parede!",
    "Não me deixe sozinho com eles!!",
    "Se correr, morre.morre",
    "Se cuide, estou em todos os lugares",
    "Você irá se arrepender disso...",
    "Também pode testar /kickme, me parece divertido.",
    "Vá incomodar em outro lugar, ninguém aqui se importa",
    "Pode correr, mas não pode se esconder.",
    "Isso é tudo que você tem?",
    "Estou bem atrás de você...",
    "Você tem companhia!",
    "Podemos fazer isso por bem ou por mal.",
    "Você não entendeu, né?",
    "É, melhor você correr!",
    "Por favor, me lembre o quanto eu me importo com isso.",
    "Eu correria mais rápido se fosse você.",
    "Isso é definitivamente o android que estamos procurando.",
    "Que a sorte esteja ao seu favor.",
    "As famosas últimas palavras",
    "E eles desapareceram para sempre, nunca devem voltar a ser vistos.",
    "\"Ah, olhe para mim! Como sou descolado, posso fugir de um bot!\" - essa pessoa",
    "Sim, sim, escreva /kickme para ver.",
    "Toma, pegue esse anel e vá a Mordor enquanto você ainda está aqui.",
    "As lendas dizem que ainda está acontecendo...",
    "Diferente de Harry Potter, seus pais não podem te protegem de mim.",
    "O medo leva a  ira. A ira leva ao ódio. O ódio ocasiona o sofriemento. Se continuar a seguir no medo, você pode "
    "ser o próximo Vader.",
    "depois de muitos cálculos, chegar a conclusão que meu interesses em suas baboseiras é 0.",
    "as lendas dizem que ainda está acontecendo...",
    "continuar assim, não tenho certeza se te queremos aqui de qualquer maneira.",
    "é um mag- Ah, Espera, Você não é Harry, continue.",
    "NÃO SE CORRE NOS CORREDORES.",
    "hasta la vista, baby.",
    "quem deixou os cachorros soltos?",
    "é engraçado porque ninguém liga.",
    "ah, que desperdício. Eu tinha gostado desse",
    "Frankly, amorzinho, eu não dou a mínima.",
    "meu milkshake arrasta todas as crianças para o pátio… Então ande mais rápido!",
    "não pode AGUENTAR a verdade!",
    "há muito tempo, em uma galáxia distante… Havia alguém que se importava com isso.. Aqui não.",
    "hey, olha pra eles! Estão correndo do inevitável ban… Que tontos.",
    "han atirou primeiro. Aí eu também.",
    "do que você vai correr depois? De um coelho branco?",
    "como diria El Doctor...Corre!",
)


SLAP_TEMPLATES = (
    "{user1} {hits} {user2} com {item}.",
    "{user1} {hits} {user2} na cara com {item}.",
    "{user1} {hits} {user2} no peito com {item}.",
    "{user1} {throws} {item} em {user2}.",
    "{user1} pega {item} e {throws} na cara de {user2}",
    "{user1} lançou {item} na cabeça de {user2}.",
    "{user1} começou a bater em {user2} com {item}.",
    "{user1} derruba {user2} e {hits} ele várias vezes com {item}.",
    "{user1} leva {item} e {hits} {user2}.",
    "{user1} amarra {user2} em uma cadeira e {throws} {item}.",
    "{user1} deu um singelo empurrão em {user2} para ensinar a nadar na lava."
)


ITEMS = (
    "uma frigideira de metal",
    "uma tocha",
    "um taco de beisebol",
    "um taco de críquete",
    "um bastão de madeira",
    "uma unha",
    "uma impressora",
    "uma pá",
    "um protetor",
    "um livro de física",
    "uma torradeira",
    "um retrato de Bolsonaro",
    "uma televisão",
    "um caminhão de 5 toneladas",
    "um tubo cheiro de cocô",
    "uma enciclopédia",
    "um laptop da xuxa",
    "uma casca de banana podre",
    "um saco de pedra",
    "uma cueca usada",
    "uma galinha de borracha",
    "um dildo gigante",
    "um extintor",
    "um pedaço de cocô petrificado",
    "uma batedeira",
    "um papel em chamas",
    "um pedaço de gelatina",
    "um osso",
    "uma vaca",
)


THROW = (
    "atira",
    "joga",
    "arremessa",
    "dispara",
)


HIT = (
    "bate em",
    "estapeia",
    "esmurra",
    "espanca",
    "balança",
)


MARKDOWN_HELP = """
Markdown é uma ferramenta de formato muito poderosa soportada pelo telegram. {} tem algumas melhorias, para ter certeza de que \
as mensagens foram guardadas corretamentes e te permite criar botões..


- <code>_italico_</code>: se colocar o texto entre ‘_' produz o texto em itálico
- <code>*negrito*</code>: se colocar o texto entre '*' produz o texto em negrito
- <code>`codigo`</code>: se colocar o texto entre '`' produz o texto monoespaçado, também conhecido como 'código'
- <code>[algumtexto](algumaURL)</code>: isso criará um link - a mensagem se mostrará em <code>algumtexto</code>, \
e clicando em cima você será levado a  página que colocou em <code>algumaURL</code>.
Ex: <code>[test](example.com)</code>


- <code>[textodobotao](botaourl:algumaURL)</code>: essa é uma melhoria especial que permite aos usuários \
ter botãos do telegram. <code>textodobotao</code> será o nome que aparecerá no botão, e <code>algumaURL</code> \
será a página da URL que abrirá ao clicar.
EX: <code>[isso é um botão](buttonurl:example.com)</code>


Se você quiser pode colocar vários botões em uma mesma linha, para isso é necessário usar :same, como aqui:
<code>[um](botaourl://example.com)
[dois](botaourl://google.com:same)</code>
Isso criará dois botões em uma mesma linha invés de um em cada uma.
"""


PortugueseStrings = {


#Connections
    "Disabled connections to this chat for users": "Conexões desabilitadas nesse chat para os usuários",
    "Enabled connections to this chat for users": "Conexões habilitadas nesse chat para os usuários",
    "Please enter on/yes/off/no in group!": "Por favor escreva on/yes/off/no no grupo!",
    "Successfully connected to *{}*": "Conectado correctamente com *{}*",
    "Connection failed!": "Conexão não sucedida!",
    "Connections to this chat not allowed!": "Conexões não permitidas neste chat!",
    "Write chat ID to connect!": "Escreva a ID do chat para conectar!",
    "Usage limited to PMs only!": "Uso limitado apenas para mensagens no privado",


#Misc
    "RUNS-K": RUN_STRINGS,
    "SLAP_TEMPLATES-K": SLAP_TEMPLATES,
    "ITEMS-K": ITEMS,
    "HIT-K": HIT,
    "THROW-K": THROW,
    "ITEMP-K": ITEMS,
    "ITEMR-K": ITEMS,
    "MARKDOWN_HELP-K": MARKDOWN_HELP,


    "The original sender, {}, has an ID of `{}`.\nThe forwarder, {}, has an ID of `{}`.":
        "O remetente, {}, tem a ID `{}`.\nO receptor, {}, tem a ID `{}`.",
    "{}'s id is `{}`.": "ID é {} - `{}`.",
    "Your id is `{}`.": "Sua ID é - `{}`.",
    "This group's id is `{}`.": "ID desse grupo é - `{}`.",


    "I can't extract a user from this.": "Não posso extrair a  ID deste usuário",
    "<b>User info</b>:": "<b>Informação do usuário</b>:",
    "\nFirst Name: {}": "\nNome: {}",
    "\nLast Name: {}": "\nASobrenome: {}",
    "\nUsername: @{}": "\nNome de usuário: @{}",
    "\nPermanent user link: {}": "\nLink permanente do usuário: {}",
    "\n\nThis person is my owner - I would never do anything against them!":
        "\n\nEssa pessoa é minha dona, eu jamais faria algo contra ela!",
    "\nThis person is one of my sudo users! Nearly as powerful as my owner - so watch it.":
        "\nEssa pessoa é uma dos meus usuários importantes! Quase com tanto poder como quem é meu dono, então tenha cuidado",
    "\nThis person is one of my support users! Not quite a sudo user, but can still gban you off the map.":
        "\nEssa pessoa é um dos meus usuários com direitos, Não é como um usuário sudo, mas pode te dar um ban global, viu? tome cuidado!",
    "\nThis person has been whitelisted! That means I'm not allowed to ban/kick them.":
        "\nEssa pessoa faz parte da lista branca. Ou seja, eu não posso banir ou kickar ela.",


    "Its always banhammer time for me!": "Sempre é hora de banhammer pra mim!",


    "It's {} in {}": "Está {} em {}",


    "Please reply to a sticker to get its ID.": "Por favor responde a um sticker para obter seu ID.",
    "Please reply to a sticker for me to upload its PNG.": "Por favor, responde a um sticker para que eu possa upar seu PNG .",


    "Write a location to check the weather.": "Escreva um lugar para eu checar o tempo lá.",
    "I will keep an eye on both happy and sad times!": "Eu estarei aqui nos tempos bons e nos tempos ruins!",
    "Today in {} is being {}, around {}°C.\n": "Hoje em {} faz {}, por volta de {}°C.\n",
    "Sorry, location not found.": "Perdão, não encontrei essa localização.",


    "Deleting identifiable data...": "Deletando dados do usuário...",


    "Try forwarding the following message to me, and you'll see!":
        "Tente encaminhar a mensagem encaminhada para mim e você verá!",
    "/save test This is a markdown test. _italics_, *bold*, `code`, [URL](example.com) [button](buttonurl:github.com) [button2](buttonurl://google.com:same)":
    """/save test Isso é um teste de markdown. _italico_, *negrito*, `codigo`, \
[URL](example.com) 
[Botão](botaourl:github.com)
[Botão2](botaourl://google.com:same)""",


#Misc GDPR
"send-gdpr": """Suas informações pessoais foram excluídas.\n\nTenha em visto que isso não vai te desbanir \
de nenhum chat, já que isso são dados do telegram, não dados do YanaBot.
flooding, advertências, e bans globais também serão mantidos, a partir de \
[isso](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/individual-rights/right-to-erasure/), "
que estabelece claramente que o direito de cancelamento não se aplica \
\"para a realização de uma tarefa feita em interesse público.\", assim como \
no caso dos dados mencionados anteriormente.""",


#Admin
"How am I meant to promote someone that's already an admin?": "Como vou promover essa pessoa a administrador se ela já é?",
"I can't promote myself! Get an admin to do it for me.": "Não posso me promover! Peça para algum administrador fazer isso, por favor.",
"Successfully promoted in *{}*!": " *{}* promovido como sucesso!",


"This person CREATED the chat, how would I demote them?": "Essa pessoa CRIOU o grupo. Como você quer que eu despromova ela?",
"Can't demote what wasn't promoted!": "Não posso despromover alguém que não é administrador!",
"I can't demote myself!": "Não posso me despromover!",
"Successfully demoted in *{}*!": " *{}* despromovido como sucesso!",
"Could not demote. I might not be admin, or the admin status was appointed by another user, so I can't act upon them!": 
"Não posso despromover essa pessoa. Pode ser que eu não seja um administrador ou foi outro administrador que promoveu ela, logo, não posso fazer nada!",


"I don't have access to the invite link, try changing my permissions!": "Não tenho acesso ao link de convite, tente mudar minhas permissões!",
"I can only give you invite links for supergroups and channels, sorry!": "Sinto muito, só posso fornecer links de convite para super grupos ou canais.",


"Admins in": "Administradores em",
"this chat": "esse chat",
" (Creator)": " (Creador)",


#AFK
"{} is now AFK!": "Agora {} está offline!",
"{} is no longer AFK!": "{} não está mais offline!",
"{} is AFK!": "{} está offline!",
"{} is AFK! says its because of: \n{}": "{} está offline! O motivo apresentado foi: \n{}",


#Antiflood
"I like to leave the flooding to natural disasters. But you, you were just a disappointment. Get out.":
     "Normalmente, tenho paciência com pessoas chatas, mas você passou do limite. Some daqui!",
"I can't kick people here, give me permissions first! Until then, I'll disable antiflood.":
    "Não posso kickar pessoas daqui, me de permissão! Enquanto eu não tiver, o antiflood estará desligado.",
"Antiflood has been disabled.": "Antiflood está desligado.",
"Antiflood has to be either 0 (disabled), or a number bigger than 3 (enabled)!":
    "Antiflood tem que ser 0 (desabilitado), ou um número superior a 3 (habilitado)!",
"Antiflood has been updated and set to {}": "Antiflood foi atualizado e mudado para {}",
"Unrecognised argument - please use a number, 'off', or 'no'.":
    "Comando desconhecido - por favor use um número, 'off', ou 'no'.",
"I'm not currently enforcing flood control!": "No momento eu não posso controlar o flood!",
"I'm currently banning users if they send more than {} consecutive messages.":
     "Estou banindo todos os usuários que enviem mais de {} mensagens consecutivas.",


#Antispam
"I've enabled antispam security in this group. This will help protect you from spammers, unsavoury characters, and the biggest trolls.":
 "Está ativada a segurança antispam no grupo. Isso te ajudará a se proteger contra spammers, pessoas desagradáveis e trolls.",


"I've disabled antispam security in this group. GBans wont affect your users anymore. You'll be less protected from any trolls and spammers though!":
    "Está desativada a segurança antispam no grupo. Os bans globais não afetarãp os usuários. Estará menos protegido de trolls e spammers!",


"Give me some arguments to choose a setting! on/off, yes/no!\n\nYour current setting is: {}\nWhen True, any gbans that happen will also happen in your group. When False, they won't, leaving you at the possible mercy of spammers.":
    "Me de alguns argumentos para estabelecer as configurações! on/off, yes/no!\n\nSua configuração atual é: {}\nQuando está True, qualquer Ban Global que aconteça também acontecerá em seu grupo. Quando está False, os Ban Globales não afetarão seu grupo, deixando ele a mercê de possíveis spammers.",


"Globally banned: <b>{}</b>": "Banido globalmente: <b>{}</b>",
"\nGlobally muted: <b>{}</b>": "\nSilenciado globalmente: <b>{}</b>",
"\nReason: {}": "\nMotivo: {}",


#Bans
    "I really wish I could ban admins...": "Como eu gostaria de poder banir administradores...",
    "I'm not gonna BAN myself, are you crazy?": "Não vou banir eu mesmo, você pirou?",
    "Banned!": "Banido!",
    "Well damn, I can't ban that user.": "Drog, não consigo banir esse usuário!",
    "You haven't specified a time to ban this user for!": 
        "Não está especificado o tempo de banimento para esse usuário!",
    "Banned! User will be banned for {}.": "Banido! Foi banido por {}.",


#Blacklist
    "<b>Current blacklisted words in {}:</b>\n": "<b>Palavras na lista negra em {}:</b>\n",
    "There are no blacklisted messages in <b>{}</b>!": "Não tem mensagens na lista negra em<b>{}</b>!",
    "Added <code>{}</code> to the blacklist in <b>{}</b>!":
        "Adicionado <code>{}</code> na lista negra em <b>{}</b>!",
    "Tell me which words you would like to add to the blacklist.":
        "Diga que palavras gostaria de adicionar na lista negra.",
    "Removed <code>{}</code> from the blacklist in <b>{}</b>!":
        "Removido <code>{}</code> da lista negra em <b>{}</b>!",
    "This isn't a blacklisted trigger...!": "Esse não é um comando da lista negrа...!",
    "None of these triggers exist, so they weren't removed.":
        "Nenhum desses comandos existe, então eles não podem ser removidos.",
    "Removed <code>{}</code> triggers from the blacklist in <b>{}</b>! {} did not exist, so were not removed.":
        "Removido <code>{}</code> dos comandos da lista negra em <b>{}</b>! {} não existe, então não foi removido.",
    "Tell me which words you would like to remove from the blacklist.":
        "Diga me quais palavras você gostaria de remover da lista negra.",


    #Filters
    "*Filters in {}:*\n": "*Filtros em {}:*\n",
    "local filters": "filtros locais",
    "*local filters:*\n": "*filtros locais:*\n",
    "No filters in {}!": "Não há filtros em {}!",
    "There is no note message - You can't JUST have buttons, you need a message to go with it!":
        "No há nenhuma mensagem - Você não pode ter botões vazios, é necessário uma mensagem que vá dentro do botão!",
    "You didn't specify what to reply with!": "Você não especificou com o que quer que eu responda!",
    "Handler '{}' added in *{}*!": "O filtro '{}' foi criado em *{}*!",
    "No filters are active in {}!": "Não há filtros ativos em {}!",
    "Yep, I'll stop replying to that in *{}*." : "Está combinado, deixarem de responder a isso em *{}*.",
    "That's not a current filter - run /filters for all active filters.":
        "Atualmente isso não é um filtro - escreve /filters para ver todos os filtros ativos.",
    
    #Disable
    "Disabled the use of `{}` in *{}*": "Desativado o uso de `{}` em *{}*",
    "That command can't be disabled": "Esse comando não pode ser desativado!",
    "What should I disable?": "O que exatamente eu deveria desativar?",


    "Enabled the use of `{}` in *{}*": "Ativado o uso de `{}` em *{}*",
    "Is that even disabled?": "Mas isso está desativado?",
    "What should I enable?": "O que exatamente eu deveria ativar?",


    "The following commands are toggleable:\n{}": "Os seguintes comandos podem ser desativados:\n{}",
    "No commands can be disabled.": "Não há comandos que podem ser desativados.",
    "No commands are disabled in *{}*!": "Não há comandos desativados em *{}*!",
    "No commands are disabled!": "Não há comandos desativados!",
    "The following commands are currently restricted in *{}*:\n{}":
        "Os seguintes comandos estão desativados em *{}*:\n{}",


#Locks
    "Locked {} messages for all non-admins!": "Bloqueada as mensagens de {} para todos os não administradores!",
    "What are you trying to lock...? Try /locktypes for the list of lockables":
        "O que você está tentando bloquear...? Escreva /locktypes para ver alista dos tipos de bloqueios.",
    "I'm not an administrator, or haven't got delete rights.":
        "Não sou um administrador ou não tenho permissão para deletar.",
    "Unlocked {} for everyone!": "Desbloqueado {} para todos!",
    "What are you trying to unlock...? Try /locktypes for the list of lockables":
        "O que está tentando desbloquear...? Escreva /locktypes para ver a lista dos tipos de bloqueios.",
    "What are you trying to unlock...?": "O que está tentando desbloquear...?",
    "I see a bot, and I've been told to stop them joining... but I'm not admin!":
        "Vejo um bot e me disseram para impedir ele de entrar... mas não sou um administrador!",
    "Only admins are allowed to add bots to this chat! Get outta here.":
        "Só é permitido aos administradores colocar bots no grupo. Saia daqui!",
    "There are no current locks in *{}*.": "Não há bloqueios em *{}*.",
    "These are the locks in *{}*:": "Esses são os bloqueios em *{}*:",
    "this chat": "este chat",


#Log channel
    "Now, forward the /setlog to the group you want to tie this channel to!":
        "Agora envie /setlog no grupo que você quer vincular esse canal!",
    "This channel has been set as the log channel for {}.": 
        "Este canal já foi configurado como o canal de registro para {}.",
    "Successfully set log channel!": "Canal de registro estabelecido com êxito!",
    "*The steps to set a log channel are:*\n • add bot to the desired channel\n • send /setlog to the channel\n • forward the /setlog to the group\n":
        """*Os passos para estabelecer um canal de registro é:*
 • botar o bot no canal que quer!)
 • escreva /setlog no canal
 • encaminhe o /setlog no grupo.""",


    "Channel has been unlinked from {}": "O canal foi desvinculado de {}",
    "Log channel has been un-set.": "Canal de registro não estabelecido.",
    "No log channel has been set yet!": "Não há nenhum canal de registro estabelecido!",


#Users
    "I've seen them in <code>{}</code> chats in total.": 
        "Eu o vi em <code>{}</code> chats no total.",
    "I've seen them in... Wow. Are they stalking me? They're in all the same places I am... oh. It's me.":
        "Eu o vi em… UAU. Está me seguindo? Você está em todos os mesmo grupos que eu… Ah. Sou eu mesmo.",
    
#Msg_deleting
    "Cannot delete all messages. The messages may be too old, I might not have delete rights, or this might not be a supergroup.":
        "Não é possível excluir todas as mensagens. As mensagens podem ser muito antigas, posso não ter direitos de deletar ou esse pode não ser um supergrupo.",
    "Purge complete.": "Purge completado.",
    "Reply to a message to select where to start purging from.":
        "Responde a uma mensagem para selecionar desde onde começar o purge.",
    "Whadya want to delete?": "O que quer apagar?",


#Muting
    "You'll need to either give me a username to mute, or reply to someone to be muted.":
        "Você precisa me dar um nome de usuário para silenciar, ou responder a mensagem da pessoa que gostaria de mutar.",
    "I'm not muting myself!": "Não vou me mutar!",
    "Afraid I can't stop an admin from talking!": "Eu me mordo porque não posso fazer um administrador parar de falar!",
    "You'll need to either give me a username to unmute, or reply to someone to be unmuted.":
        "Você precisa me dar um nome de usuário para desmutar, ou responder a mensagem da pessoa que gostaria de desmutar.",
    "This user already has the right to speak in {}.": "Esse usuário agora pode falar em {}.",
    "Yep, {} can start talking again in {}!": "Sim, {} pode voltar a falar em {}!",
    "This user isn't even in the chat, unmuting them won't make them talk more than they already do!":
        "Esse usuário nem está mais no grupo, desmutar ele não fará ele falar mais do que já está falando!",
    "I really wish I could mute admins...": "Como eu gostaria de poder silenciar administradores...",
    "I'm not gonna MUTE myself, are you crazy?" : "Não vou mutar a MIM MESMA, o que se passa na sua cabeça?",
    "You haven't specified a time to mute this user for!":
        "Você não disse quanto tempo devo deixar silenciado esse usuário!",
    "Muted for {} in {}!": "Silenciado durante {} em{}!",
    "This user is already muted in {}!": "Este usuário agora está silenciado.",
    "Well damn, I can't mute that user.": "Droga, não posso silenciar esse usuário.",


    "You'll need to either give me a username to restrict, or reply to someone to be restricted.":
        "Você precisa me dar um nome de usuário para restringir, ou responder a mensagem da pessoa que gostaria de restringir.",
    "I'm not restricting myself!": "Não vou me restringir!",
    "Afraid I can't restrict admins!": "Eu me mordo porque não posso restringir um administrador!",
    "{} is restricted from sending media in {}!": "{} foi restringido de enviar mídia em {}!",
    "This user is already restricted in {}!": "Esse usuário já está restringido em {}!",
    "This user isn't in the {}!": "Esse usuário não está em {}!",


    "You'll need to either give me a username to unrestrict, or reply to someone to be unrestricted.":
        "Você precisa me dar um nome de usuário para retirar a restrição, ou responder alguma mensagem dessa pessoa.",
    "This user already has the rights to send anything in {}.": 
        "Este usuário já tem permissões para enviar qualquer coisa em {}.",
    "Yep, {} can send media again in {}!": "Sim, {} pode voltar a enviar mídia em {}!",
    "This user isn't even in the chat, unrestricting them won't make them send anything than they already do!":
        "Esse usuário nem sequer está nesse grupo..",
    "I really wish I could restrict admins...": "Como eu gostaria de poder restringir administradores…",
    "I'm not gonna RESTRICT myself, are you crazy?": "Eu não vou ME restringir, o que se passa na sua cabeça?",
    "You haven't specified a time to restrict this user for!": 
        "Você não especificou o tempo que deve restringir esse usuário!",
    "Well damn, I can't restrict that user.": "Droga, não posso restringir esse usuário.",
    "{} is muted in {}!": "{} está silenciado em {}!",
    "Restricted from sending media for {} in {}!": "Restringido para enviar mídia por {} em {}!",
    "Restricted for {} in {}!": "{} Restringido por {} em {}!",


#Notes
    "Get rekt": "Destruo você!.",




#Multi
    "Invalid Chat ID provided!": "O ID do chat não é válido!", #Connections
    "You don't seem to be referring to a user.": "Parece que você não está se referindo a nenhum usuário.", #Admin, Bans, Muting
    "I can't seem to find this user": "Parece que não posso encontrar esse usuário.", #Bans, Muting
    "Yes": "Sim", #Antispam
    "No": "Não", #Antispam


#__main__
    #Module names
        "Admin": "Administrador",
        "AFK": "Ausente (AFK)",
        "AntiFlood": "Antiflood",
        "Bans": "Bans",
        "Word Blacklists": "Lista negra",
        "Filters": "Filtros",
        "Command disabling": "Desativar comandos",
        "Antispam security": "Segurança antispam",
        "Locks": "Locks",
        "Log Channels": "Registro de canais",
        "Misc": "Diversos",
        "Purges": "Purges",
        "Muting & Restricting": "Silenciar e Restringir",
        "Notes": "Notas",
        "Reporting": "Reportar",
        "RSS Feed": "Feed RSS",
        "Rules": "Regras",
        "Connections": "Conexões",
        "Bios and Abouts": "Biografía",
        "Warnings": "Advertências",
        "Welcomes/Goodbyes": "Boas vindas/Despedidas",


#Some main stuff
"Here is the help for the *{}* module:\n{}": "Aqui está a ajuda para o módulo de *{}*:\n{}",
"Back": "Atrás",


"send-start": """Olá {}, me chamo {}! Se tiver alguma pergunta sobre como me usar, use /help - e depois vá ao @NotAvaibleYet. 


Sou um bot para administrar grupos mantido por [esta maravillosa persona](tg://user?id={}). Sou parecido com a [Marie](https://github.com/PaulSonOfLars/tgbot) 
Foi feito pelo python3, usando a biblioteca de \
python-telegram-bot, e sou totalmente de código aberto - pode ver o que me faz funcionar \
[aqui](https://gitlab.com/MrYacha/pYanaBot-2.0)!


Sinta se livre para enviar sugestões em GitHub, ou contatar ao meu criador em meu grupo de suporte, @YanaBotGroup, como bugs, perguntas \
ou propostas de funcionamento que pode ter :)


Se você gosta de me usar e/ou quer me ajudar a sobreviver às tempestades, pressione /donate para ajudar a pagar/atualizar meu VPS!""",


    "send-help": """Olá! Meu nome é *{}*.
Sou um bot de gestão de grupos com alguns extras divertidos! Dê uma olhada abaixo para ter uma ideia de algumas coisas em que posso ajudá-lo.


Comandos principais disponíveis:
 - /start: inicia o bot
 - /help: te envia uma mensagem no privado com informações.
 - /help <module name>: te envia uma mensagem no privado com as informações desse comando.
 - /donate: informações sobre como doar!
 - /lang: Muda o idioma do bot 
 - /settings:
   - em mensagem privada: te enviará a configuração de todos os módulos disponíveis.
   - no grupo: te redireciona a uma mensagem privada, com todas as configurações do grupo.
   {}
   """,


    "send-group-settings": """Olá! Há algumas configurações disponíveis para *{}* - entre e selecione aquilo em que
está interessado.""",


#Misc
"RUNS-K": RUN_STRINGS,
"SLAP_TEMPLATES-K": SLAP_TEMPLATES,
"ITEMS-K": ITEMS,
"HIT-K": HIT,
"THROW-K": THROW,
"ITEMP-K": ITEMS,
"ITEMR-K": ITEMS,
"MARKDOWN_HELP-K": MARKDOWN_HELP,


#GDPR
"send-gdpr": """Sua informaão personal foi apagada.\n\nTenha em mente que isso não vai de desbanir  \
de nenhum chat, já que isso são dados do Telegram, NÃO dados de YanaBot.
Flooding, advertências e bans globais también se preservam, a partir de \
[isso](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/individual-rights/right-to-erasure/), "
que estabelece claramente que o direito de cancelamento não se aplica \
\"para a realização de uma tarefa realizada em interesse público.\", assim como \
no caso dos dados mencionados anteriormente.""",




#Help modules
"Admin_help": """
 - /adminlist | /admins: lista dos administradores do grupo


*Solo administradores:*
 - /pin: Fixa silenciosamente a mensagem que foi respondida: coloque ‘loud’ ou ‘notify’ par notificar os usuários, caso seja de seu interesse. 
 - /unpin: Desfixa a mensagem respondida.
 - /invitelink: Gera o link de convite ao grupo
 - /promote: Dá o cargo de administrador ao usuário que foi respondido
 - /demote: Tira o cargo de administrador do usuário que foi respondido
""",


"AFK_help": """
 - /afk <motivo>: Te marca como offline.
 - brb <motivo>: Faz o mesmo que o comando AFK mas sem ser um comando. 


Quando está ausente (AFK), qualquer menção será respondida con uma mensagem que diz que não está disponível.
""",


"AntiFlood_help": """
 - /flood: Te mostro o controle antiflood atual.


*Solo administradores:*
 - /setflood <int/'no'/'off'>: Ativa ou desativa o controle de flood
""",


"Antispam security_help": """
*Solo administradores:*
 - /antispam <on/off/yes/no>: Desabilitar a segurança antispam no grupo ou te mostra a sua configuração atual.


Os proprietários do bot sugerem utilizar o antispam para proibir spammers em todos os grupos. Isso ajuda a proteger \
você e seus grupos por conta da eliminação mais rápida possível de spammers. É possível desativar em um grupo escrevendo \
/antispam
""",


"Bans_help": """
 - /kickme: Expulsa o usuário que escreve este comando


*Solo administradores:*
 - /ban <userhandle>: bane o usuário. (deve ser dado o nome de usuário, ou respondendo a mensagem dele)
 - /tban <userhandle> x(m/h/d): bane o usuário durante x tempo. (deve ser dado o nome de usuário, ou respondendo a mensagem dele). m = minutos, h = horas, d = dias.
 - /unban <userhandle>: desbane o usuário.  (deve ser dado o nome de usuário, ou respondendo a mensagem dele)
 - /kick <userhandle>: expulsa o usuário.  (deve ser dado o nome de usuário, ou respondendo a mensagem dele)
""",


"Connections_help": """
Ações disponíveis mediante a grupos conectados:
 • Ver e editar notas
 • Ver e editar filtros
 • Ver e editar a lista negra
 • Promover/remover administrador
 • Ver a lista de administradores, ver link de convite
 • Desativar/ativar comandos no chat
 • Silenciar/remover silêncio a usuários no chat
 • Restringir/remover restrição a usuários no chat
 •Mais no futuro!


 - /connection <iddelchat>: Conecta ao chat remoto
 - /disconnect: Desconecta do chat
 - /allowconnect on/yes/off/no: Permite aos usuarios se conectarem ao grupo
""",


"Filters_help": """
 - /filters: Lista de todos os filtros no chat.


*Solo administradores:*
 - /filter <palavra chave> <mensagem com a qual ele responde>: adiciona um filtro a este chat. O bot responderá a esta mensagem quando é mencionado\
A 'palavra chave'. Se responder um sticker com uma palavra chave, o bot responderá a  palavra chave com este sticker. NOTA: todas as palavras \
chave dos filtros estão em minúsculo. Se queira que sua palavra chave seja uma frase, use aspas. ex: /filter "ei ola" Tudo bem? \
como vai?
 - /stop <palavra chave>: elimina o filtro.
""",


"Command disabling_help": """
 - /cmds: verifica o estado atual dos comandos desabilitados.


*Solo administradores:*
 - /enable <nome do comando>: ativa este comando
 - /disable <nome do comando>: desativa esse comando
 - /listcmds: lista de todos os comandos que se pode ativar o desativar
""",


"Locks_help": """
 - /locktypes: lista de todos os tipos de os bloqueios possíveis


*Solo administradores:*
 - /lock <tipo>: bloqueia elementos de um determinado tipo (não disponível em chat privado)
 - /unlock <tipo>: desbloqueia elementos de um determinado tipo (não disponível em chat privado)
 - /locks: mostra a lista atual de bloqueios no  chat


Os bloqueios podem ser utilizados para restringir os usuários em um grupo.
ex:
Bloquear URL apagará automáticamente todas as mensagens que contenham URLs e que não tenham sido colocados na  lista branca, bloquear stickers apagará todos os \
stickers etc.
Bloquear os bots fará que nenhum usuário que não seja administrador possa adicionar bots ao chat.
""",


"Log Channels_help": """
*Solo administradores:*
- /logchannel: obtém informação do registro do canal.
- /setlog: configura o canal de registro.
- /unsetlog: elimina o canal de registro.


Para configurar o canal de registro se faz da seguinte forma:
- adicione o bot ao canal desejado (como administrador!)
- escrever /setlog no canal
- envie o /setlog no grupo
""",


"Misc_help": """
 - /id: obtém a id do grupo. Se usada respondendo uma mensagem, obtém a id  deste usuário.
 - /runs: responde uma frase aleatória de uma bateria de frases pré-estabelecidas.
 - /slap: estapeia um usuário, ou recebe um tapa se não foi utilizado como resposta.
 - /time <lugar>: te dá a hora para o lugar indicado.
 - /weather <cidade>: mostra o tempo climático para a cidade indicada.
 - /info: obtém informação de um usuário.
 - /gdpr: apaga suas informações da base de dados do bot. Apenas no privado.
 - /stickerid: responda a um sticker com isso e te darei a ID do arquivo.
 - /getsticker: responda a um sticker com isso e farei o upload do arquivo em PNG.


 - /markdownhelp: resumo rápido de como funciona o markdown no telegram - apenas usável em chats privados.
""",


"Purges_help": """
*Solo administradores:*
 - /del: apaga a mensagem que é respondida.
 - /purge: apaga todas as mensagens anteriores da mensagem respondida.
 - /purge <número X>: apaga a mensagem respondida, e as  X mensagens seguintes.
""",


"Muting & Restricting_help": """
*Solo administradores:*
 - /mute <userhandle>: silencia um usuário. Pode ser usado respondendo uma mensagem, silenciando o usuário que foi respondido.
 - /tmute <userhandle> x(m/h/d): silencia um usuário durante x tempo. (via nome de usuário ou respondendo a uma mensagem sua). m = minutos, h = horas, d = dias.
 - /unmute <userhandle>: retira o silêncio de um usuário. Pode ser usado como resposta, retirando o silêncio do usuário a que responde.
 - /restrict <userhandle>: restringe um usuário de enviar stickers, gif, links ou mídia. Pode ser usado como resposta, restringindo o usuário a que responde.
 - /trestrict <userhandle> x(m/h/d): restringe um usuário durante x tempo. (via nome de usuário ou respondendo a uma mensagem sua). m = minutos, h = horas, d = días.
 - /unrestrict <userhandle>: retira a restrição de um usuário para enviar stickers, gif, links ou mídia. Pode ser usado como resposta, retirando a restrição ao usuário a que responde.
""",


"Notes_help": """
 - /get <nomedanota>: obtém a nota guardada com este nome
 - #<nomedanota>: o mesmo que o /get
 - /notes o /saved: lista de todas as notas guardadas no chat.


Se quer recuperar o conteúdo de uma nota sem formato, utilize `/get <nomedanota> noformat`. Isto pode \
ser útil quando atualiza uma nota, especialmente se houver botões nela.


*Solo administradores:*
 - /save <nomedanota> <conteudodanota>: guarda 'conteudodanota' como nota com o nome 'nomedanota'
Se pode adicionar botões as notas usando a sintaxe normal de 'markdown' - o link que adicionar ao botão deverá levar antes \
`buttonurl:` tal como mostrado aqui: `[textodelbotón](buttonurl:tulink.com)`. Assim permaneceria configurado um botão em uma nota. Olhe /markdownhelp para mais informação.
 - /save <nomedanota>: salva a mensagem a ser respondida com 'nomedanota'
 - /clear <nomedanota>: apaga a nota com esse nome
""",


"Reporting_help":"""
 - /report <motivo>: responda a uma mensagem para reportar aos administradores.
 - @admin: responde uma mensagem para reportar aos administradores.
NOTA: nenhum desses comandos se ativará se utilizado pelos administradores


*Solo administradores*
 - /reports <on/off>: muda a configuração dos reportes, ou te permite ver o estado atual da configuração.
   - Se feito em mensagem privada, muda seu status.
   - Se feito em uma chat, muda o status do chat.
""",


"RSS Feed_help": """
 - /addrss <link>: adiciona um link RSS às inscrições.
 - /removerss <link>: para um link RSS das inscrições.
 - /rss <link>: mostra os dados do link e a última entrada, serve sobretudo para fazer testes.
 - /listrss: mostra a lista de feeds RSS aos que o chat está inscrito.


NOTA: nos grupos, apenas os administradores podem adicionar/apagar links RSS das inscrições do grupo.
""",


"Rules_help": """
 - /rules: te mostra as regras para este chat


*Solo administradores:*
 - /setrules <suas regras aqui>: configura as regras de um chat.
 - /clearrules: apaga as regras do chat em que está.
""",


"Sed/Regex_help": """
 - s/<text1>/<text2>(/<flag>): Responda a uma mensagem com isto para fazer uma operação sed nesta mensagem, mudando todas \
As coisas de 'text1' com 'text2'. Flags são opcionais, e atualmente incluem 'i' para ignorar, 'g' para global, \
ou nada.Os delimitadores incluem `/`, `_`, `|`, y `:`. É suportada uma agrupação de texto. A mensagem resultante não pode ser \
mais comprido que {}.


*Recordatorio:* Sed usa alguns caracteres especiais para facilitar a comparação, como isto: `+*.?\\`
Se quer usar esses caracteres, assegure-se de que não os incluam!
eg: `\\?`.
""",


"Bios and Abouts_help": """
 - /setbio <texto>: respondendo um usuário, salvando sua biografía.
 - /bio: mostrará sua biografia ou a de outro usuário. 
 - /setme <texto>: mostra suas informações.
 - /me: te mostrará sua biografia ou a de outro usuário.
""",


"Warnings_help": """
 - /warns <userhandle>: te mostra o número de advertências e a razão do usuário que foi respondido
 - /warnlist: lista dos filtros de advertências atuais.


*Solo administradores:*
 - /warn <userhandle>: adverte um usuário. Depois de 3 advertências, o usuário será banido do grupo. Pode ser usado respondendo uma mensagem.
 - /resetwarn <userhandle>: Reseta as advertências para um usuário. Pode ser usado respondendo uma mensagem.
 - /addwarn <palavrachave> <mensagem adicional>: estabelece um filtro de advertência em uma determinada palavra chave. Se quer que sua palavra chave \
seja uma frase, ponha entre aspas, como aquí: `/addwarn "muito nervoso" Este é um usuário nervoso`. 
 - /nowarn <palavrachave>: para um filtro de advertência
 - /warnlimit <num>: estabelece um número limite de advertências
 - /strongwarn <on/yes/off/no>: Se está no on e exceda o número de advertências, o usuário será banido. Senão ele só será expulso.
""",


"Welcomes/Goodbyes_help": """
Suas mensagens de Bem-vindo/despedida no grupo podem ser personalizadas de múltiplas formas. Se queira que as mensagens sejam individuais\
como mensagem predefinida, siga esses passos:
 - `{{first}}`: isto representa o *nome* do usuário
 - `{{last}}`: isto representa o *sobrenome* do usuário. É predefinido o *nome* se o usuário não tem sobrenome.
 - `{{fullname}}`: isto representa o nome *completo*. Por padrão o *nome* de usuário apenas , se não tiver sobrenome.
 - `{{username}}`: isto representa o *user*. Por padrão *menciona* o nome do usuário caso não tenha apelido.
 - `{{mention}}`: este apenas *menciona* a um usuário - escrevendo unicamente seu nome.
 - `{{id}}`: isto representa o *id* do usuário.
 - `{{count}}`: isto representa o *número* do membro*.
 - `{{chatname}}`: isto representa o *nome do grupo atual*.
Cada variável DEVE ser colocada entre `{{}}` para que seja substituída.
As mensagens de bem-vindo suportam markdown, assim você pode fazer com que qualquer palavra venha em negrito/itálico/monoespaçado/links. \
Também pode-se colocar botões, assim pode-se fazer que as bem-vindas fiquem espetaculares com botões de introdução. \
Para criar um botão que leve a suas normas, use isso: `[Normas](buttonurl://t.me/{}?start=group_id)`. \
Simplesmente substitua o `group_id` com a ID do seu grupo, que você pode obter via /id,  e aparecerá. \
Lembre-se de que os IDs de grupo geralmente são precedidos pelo sinal `-`; Esse sinal É NECESSÁRIO, então por favor \
não apague. \
Se você tiver humor suficiente, também pode colocar imagens / vídeos / gif / notas de voz como uma mensagem de boas-vindas, \
respondendo à mensagem com a imagem / gif / vídeo com /setwelcome.


*Solo administradores:*
 - /welcome <on/off>: ativa/desativa as mensagens de bem-vindo.
 - /welcome: mostra os ajustes de bem-vindo atuais.
 - /welcome noformat: mostra o bem-vindo atual, porém sem formato - útil se quiser editar uma mensagem de bem-vindo!
 - /goodbye ->o mesmo que para /welcome.
 - /setwelcome <algumtexto>: configure sua mensagem de boas-vindas. Se usado em resposta à mídia, defina imagem / gif / vídeo como bem-vindo.
 - /setgoodbye <algumtexto>: o mesmo que /setwelcome porém para despedidas.
 - /resetwelcome: reseta a mensagem de bem-vindo para mensagem padrão.
 - /resetgoodbye: reseta a mensagem de despedida para mensagem padrão.
 - /cleanwelcome <on/off>: Para novos membros chegando, tenta excluir as mensagens de boas-vindas anteriores, evitando assim o spam de mensagens de boas-vindas no chat.
- /cleanservice <on/off/yes/no>: exclue mensagens de serviço; aquelas mensagens como "x se juntou ao grupo" que são vistas quando alguém se junta.
 - /welcomesecurity <off/soft/hard>: soft - 
restringe as permissões do usuário que acabou de entrar, para que ele não possa enviar mídia por 24 horas, hard - restringe as permissões do usuário para enviar mensagens até que ele clique na mensagem "Eu não sou um bot.\"
"""
}
