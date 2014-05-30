cd ~/Desktop/
mkdir BukkitServer
cd BukkitServer/
curl -LO http://cbukk.it/craftbukkit-beta.jar
echo "cd ~/Desktop/BukkitServer/" >> start.command
echo " java -Xmx1024M -jar craftbukkit-beta.jar -o true" >> start.command
chmod +x start.command