##
## EPITECH PROJECT, 2019
## arcade
## File description:
## nique tout
##

RM = rm -f

NAME = challenge01

$(NAME):
	cp ./src/challenge01.py challenge01
	chmod 755 challenge01
	cp ./src/challenge02.py challenge02
	chmod 755 challenge02
	cp ./src/challenge03.py challenge03
	chmod 755 challenge03
	cp ./src/challenge04.py challenge04
	chmod 755 challenge04
	cp ./src/challenge05.py challenge05
	chmod 755 challenge05
	cp ./src/challenge06.py challenge06
	chmod 755 challenge06
	cp ./src/challenge07.py challenge07
	chmod 755 challenge07
	cp ./src/challenge08.py challenge08
	chmod 755 challenge08
	cp ./src/challenge09.py challenge09
	chmod 755 challenge09
	cp ./src/challenge10.py challenge10
	chmod 755 challenge10
	cp ./src/challenge11.py challenge11
	chmod 755 challenge11
	cp ./src/challenge12.py challenge12
	chmod 755 challenge12
	cp ./src/challenge13.py challenge13
	chmod 755 challenge13
	cp ./src/challenge14.py challenge14
	chmod 755 challenge14

all: $(NAME)

fclean:
	$(RM) challenge01
	$(RM) challenge02
	$(RM) challenge03
	$(RM) challenge04
	$(RM) challenge05
	$(RM) challenge06
	$(RM) challenge07
	$(RM) challenge08
	$(RM) challenge09
	$(RM) challenge10
	$(RM) challenge11
	$(RM) challenge12
	$(RM) challenge13
	$(RM) challenge14

re: fclean all
