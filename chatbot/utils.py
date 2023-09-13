class BotUtils:
    @staticmethod
    def bot_response(user_message: str):
        link = BotUtils._get_raw_url(user_message)
        
        if not link:
            return  "O endereço enviado está em um formato inválido. \U0000274C \nVerifique se o link informado está correto."
        
        image_id = BotUtils._get_image_id(link)
        downloadable_url = BotUtils._generate_downloadable_url(image_id)
        return  f"Seu link para download está pronto! \U00002705 \n{downloadable_url}"

    @staticmethod
    def _get_raw_url(user_message: str):
        link = user_message.split(" ")[-1]
        isValid = link.find(".htm")
        return False if (isValid == -1) else link

    @staticmethod
    def _get_image_id(link: str):
        image_id = link.split("_")[-1].split(".")[0]
        return image_id
    
    @staticmethod
    def _generate_downloadable_url(image_id: str):
        image_URL = f"https://br.freepik.com/download-file/{image_id}"
        return image_URL
