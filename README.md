# Dead Weight Discord Bot 

@sambarrett23072's first discord bot

This bot has one very simple function, it will post the "now we've got rid of the dead weight and tag a game role" into a discord server when a member leaves the associated channel.

## How to Run
1. Ensure you have docker installed on the host machine 
2. Pull the repo ```git clone https://github.com/sambarrett23072/Dead-Weight``` Note: it will create it's own directory called Dead-Weight
3. Create a .env file, and insert the following ```DISCORD_TOKEN={TOKEN}```
4. Build the docker container with the command ```docker build -t dead-weight .``` Note: may require sudo
5. Run the docker container with the command ```docker run -d --restart unless-stopped dead-weight``` Note: may require sudo

Feauture Roadmap 
https://github.com/sambarrett23072/Dead-Weight/milestones
