echo "Instalando docker"
sudo apt-get update && sudo apt upgrade -y
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo gpasswd -a $USER docker
echo "docker instalado consucesso!!"
echo "instalando docker compose..."
sudo apt-get install ca-certificates curl gnupg
sudo apt-get install docker-compose-plugin
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
sudo mkdir -p $DOCKER_CONFIG/cli-plugins
sudo curl -SL https://github.com/docker/compose/releases/download/v2.17.2/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
sudo chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
echo "docker compose instalado"
docker compose version
echo instalando a imagem e subindo o container
docker compose build