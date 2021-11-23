

int hash = super.getHash(key);
HashItem<K,V> slot = _items.get(hash);
while(!slot.isTrueEmpty() && slot.getKey() != key) {  
    hash = (hash+1)%_items.size(); //linear probing
    slot = _items.get(hash);
}

//case 1: slot exist and key equals and we just update the value
slot.setValue(value);

//case 2: slot marked deleted, but key equals then we update the value and mark it exist
slot.setValue(value);
slot.setIsEmpty(false);//in case the slot previously marked deleted.
_number_of_elements++; //++size because we just marked it exists

//case 3: slot is truly empty
slot.setKey(key); 
slot.setValue(value);
slot.setIsEmpty(false);
_number_of_elements++;//++size because we marked it exists


//the while loop stop when slot is true empty and slot.getkey == key parameter

//slot.isEmpty() 
//boolean falg = False
//slot contains value and keys

//slot.isTrueEmpty()
//no key, no val, flag =false
