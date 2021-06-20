var selected = false;

function selectable(elem){
    if(elem.dropped) return;
    if(selected) selected.classList.remove('selected-block');
    if(selected == elem) {
        selected = false; 
        return;
    }
    
    selected = elem;
    selected.classList.add('selected-block');
}

function dropable(elem, index){
    if(!selected) return;
    if(elem.noSpace) return;

    //append
    selected.classList.add('pin');
    selected.appendChild(hiddenInput(index, selected.getAttribute('value')));
    elem.appendChild(selected);

    //reset 
    selected.classList.remove('selected-block');
    selected.dropped = true;
    selected = false;
    elem.noSpace = true;
}

function multiDropable(elem, index){
    if(!selected) return;
    if(elem.noSpace) return;
    if(selected.droppedBefore) return dropable(elem, index);

    //clone
    let cln = selected.cloneNode(true);
    cln.dropped = true;
    cln.classList.add('pin');
    cln.classList.remove('selected-block');

    //append
    cln.appendChild(hiddenInput(index, cln.getAttribute('value')))
    elem.appendChild(cln);

    //reset
    selected.droppedBefore = true
    elem.noSpace = true;
}


function hiddenInput(index, value){
    let input = document.createElement("INPUT");
    input.setAttribute("type", "hidden");
    input.setAttribute("value", value);
    input.setAttribute("name", "block" + index);

    return input;
}



