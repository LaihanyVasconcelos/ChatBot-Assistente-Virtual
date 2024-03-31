#ChatBot Básico com perguntas e respostas para assistencia tecnica e novidades de para ou de uma empresa. ♥

import os

def processar_respostas(resposta,nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, aqui está algumas opções: \n • Reinicie os dispositivos de rede: Isso inclui o roteador, modem e qualquer outro dispositivo de rede. Às vezes, problemas de rede podem ser corrigidos simplesmente reiniciando esses dispositivos.\n • Verifique as conexões físicas: Certifique-se de que todos os cabos de rede estejam firmemente conectados aos dispositivos corretos e que não haja cabos danificados.\n • Ajuste as configurações do software: Alguns programas oferecem opções de configuração que podem ser ajustadas para melhorar o desempenho. Verifique as configurações do software e faça ajustes conforme necessário.\n • Verifique as luzes indicadoras nos dispositivos de rede: Muitos dispositivos de rede têm luzes indicadoras que mostram se estão funcionando corretamente. Verifique se as luzes correspondentes estão acesas e se há algum padrão que indique um problema específico.\n • Reinicie o computador ou dispositivo: Às vezes, problemas de rede podem ser resolvidos reiniciando o dispositivo que está tendo problemas de conexão.\n • Entre em contato com o provedor de serviços de Internet (ISP): Se nenhum dos passos acima resolver o problema, pode ser necessário entrar em contato com o provedor de serviços de Internet para verificar se há problemas de conexão mais amplos na área ou se há problemas específicos com sua conexão.\n • Procure assistência técnica: Se o problema persistir, entre em contato com o suporte técnico da sua empresa de TI ou provedor de serviços de Internet para obter ajuda adicional. Eles podem fornecer orientação mais específica com base no seu problema. {os.linesep} ') 
    elif resposta == '2':
        print(f'{os.linesep}{nome}, aqui está algumas opções: \n • Verifique os requisitos de sistema: Certifique-se de que o seu sistema atenda aos requisitos mínimos de hardware e software do programa. Se o seu sistema estiver abaixo dos requisitos recomendados, pode afetar o desempenho do software.\n • Feche outros programas: Se estiver executando muitos programas ao mesmo tempo, isso pode sobrecarregar o sistema e afetar o desempenho do software específico. Tente fechar outros programas que não estão em uso para liberar recursos do sistema.\n • Reinstale o software: Se o problema persistir, tente desinstalar e reinstalar o software. Isso pode corrigir problemas de instalação corrompida ou arquivos danificados que podem estar afetando o desempenho.\n • Contate o suporte técnico: Se nenhuma das soluções acima resolver o problema, entre em contato com o suporte técnico do software. Eles podem fornecer assistência adicional e orientação específica para resolver o problema de desempenho que está enfrentando. {os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, aqui esta a opções que poderá te ajudar: \n • Entre em contato com a nossa assistencia tecnica via WhatsApp (83) 9 5555-3333.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, aqui está as ultimas notícias e atualizações sobre tecnologia: \n • Olá! Temos ótimas novidades sobre as últimas atualizações em tecnologia da nossa empresa de TI. Estamos constantemente aprimorando nossos produtos e serviços para oferecer soluções ainda mais eficientes e inovadoras aos nossos clientes. As atualizações mais recentes incluem melhorias de desempenho, novos recursos e aprimoramentos de segurança em nossos softwares e sistemas. Além disso, estamos expandindo nossa oferta para incluir tecnologias emergentes, como inteligência artificial, aprendizado de máquina e computação em nuvem, para atender às crescentes demandas do mercado. Estamos empolgados em compartilhar essas novidades e continuaremos trabalhando duro para fornecer soluções de ponta que impulsionem o sucesso de nossos clientes. Fique ligado para mais atualizações emocionantes em breve!.{os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep}{nome}, aqui estão algumas soluções que podemos oferecer para ajudar a proteger sua empresa ou seus dados pessoais: \n • Auditoria de Segurança: Podemos realizar uma auditoria abrangente de segurança cibernética em sua rede, identificando vulnerabilidades e áreas de risco.\n • Implementação de Firewalls e Antivírus: Configuraremos firewalls robustos e software antivírus para proteger sua rede contra ataques de malware e intrusões.\n • Treinamento de Conscientização em Segurança: Oferecemos programas de treinamento para funcionários, visando aumentar a conscientização sobre ameaças cibernéticas e melhores práticas de segurança.\n • Monitoramento em Tempo Real: Implementaremos sistemas de monitoramento em tempo real para detectar e responder a atividades suspeitas em sua rede.\n • Backup e Recuperação de Dados: Configuraremos políticas de backup automáticas e sistemas de recuperação de desastres para garantir que seus dados estejam protegidos contra perdas.\n • Gestão de Identidade e Acesso: Implementaremos soluções de gestão de identidade e acesso para garantir que apenas usuários autorizados tenham acesso aos seus sistemas e dados.\n • Criptografia de Dados: Implementaremos medidas de criptografia para proteger seus dados confidenciais durante a transmissão e armazenamento. {os.linesep} \n') 
    else:
        print('Digite apenas 1, 2, 3, 4 ou 5')
        
def start ():
    #Me apresentar pelo ChatBot
    print('Óla! Bem-vindo(a)')
    #Pedir o nome
    nome = input('Digite seu nome:')
    #Pedir o email
    email = input ('Digite seu email:')
    while True:
        #Oferecer o menu de opções de perguntas
        resposta = input(
        f'Qual é o problema técnico com o qual você precisa de ajuda hoje?'
        f'{os.linesep}[1] - Você está enfrentando problemas de rede?'
        f'{os.linesep}[2] - Você está enfrentando problemas de desempenho com algum software específico?'
        f'{os.linesep}[3] - Você precisa de assistência com a instalação de algum software com assistência tecnica remota?'
        f'{os.linesep}[4] - Você gostaria de receber nossas últimas notícias e atualizações sobre tecnologia?'
        f'{os.linesep}[5] - Você está procurando por soluções de segurança cibernética?{os.linesep}')
        #Processar a resposta enviada
        processar_respostas(resposta, nome) 

if __name__=='__main__' :
    start()
