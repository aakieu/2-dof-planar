void SetJointZero(int deg){ 
  int x = map(deg,0,180,zero_low, zero_high);
  SetPosition(13,x); 
};

void SetJointOne(int deg){
  int x = map(deg,-90,90,one_low, one_high);
  SetPosition(0,x); 
};
