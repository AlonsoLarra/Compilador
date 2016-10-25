MAIN(){
VAR n.
VAR first.
VAR second.
VAR index.
VAR next.
VAR palabra.
palabra='hola'.
n=5.
first=0.
second=1.
index=0.
CYC(n){
CON(index<2){
next=index.
}
CON(index>1){
next=SUM(first,second).
first=second.
second=next.
}
}
}