1) cd ~/repos
2) git clone https://github.com/phaustin/importtest.git importtest
3) cd ~
4) Then do:

executing::
  
   > python ~/repos/importtest/main.py

Produces::

   -------- inside main program

   --------------inside function levelB2fun
   called from module importtest.levelA.levelB.Bgroup

   ---------inside function levelA1fun
   called from module importtest.levelA.Agroup

   ---------exit function levelA1fun

   ---------inside function levelA2fun
   called from module importtest.levelA.Agroup

   ---------exit function levelA2fun

   --------------inside function levelB1fun
   called from module importtest.levelA.levelB.Bgroup

   --------------exit function levelB1fun

   --------------exit function levelB2fun

   -------- exit main program
