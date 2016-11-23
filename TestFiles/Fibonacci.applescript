MAIN(){
VAR first.
VAR second.
VAR index.
VAR next.
first=0.
second=1.
index=0.
CYC(5){
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