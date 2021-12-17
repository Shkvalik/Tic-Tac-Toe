var t = new Array(9);

function ai() { //AI algorithm
  var id = Math.floor(Math.random() * 9); //choose random place
  t[id] ? ai() : move(id, 'ai'); //ai move

}

function checkEnd() { // Check win combination(dirty code)
  if (t[0]=='ai' && t[1]=='ai' && t[2]=='ai' || t[0]=='player' && t[1]=='player' && t[2]=='player')  return true;
  if (t[3]=='ai' && t[4]=='ai' && t[5]=='ai' || t[3]=='player' && t[4]=='player' && t[5]=='player')  return true;
  if (t[6]=='ai' && t[7]=='ai' && t[8]=='ai' || t[6]=='player' && t[7]=='player' && t[8]=='player')  return true;
  if (t[0]=='ai' && t[3]=='ai' && t[6]=='ai' || t[0]=='player' && t[3]=='player' && t[6]=='player')  return true;
  if (t[1]=='ai' && t[4]=='ai' && t[7]=='ai' || t[1]=='player' && t[4]=='player' && t[7]=='player')  return true;
  if (t[2]=='ai' && t[5]=='ai' && t[8]=='ai' || t[2]=='player' && t[5]=='player' && t[8]=='player')  return true;
  if (t[0]=='ai' && t[4]=='ai' && t[8]=='ai' || t[0]=='player' && t[4]=='player' && t[8]=='player')  return true;
  if (t[2]=='ai' && t[4]=='ai' && t[6]=='ai' || t[2]=='player' && t[4]=='player' && t[6]=='player')  return true;
  if(t[0] && t[1] && t[2] && t[3] && t[4] && t[5] && t[6] && t[7] && t[8]) return true;
}

function move(id, role) {
  if(t[id]) { //condition if cell is set
    alert('Упс! Клетка занята')
    return false
  }
  t[id] = role;
  document.getElementById(id).className = 'cell ' + role;
  !checkEnd() ? (role === 'player') ? ai() : null : reset()
}

function reset() { //reset game
  var winner = (t.filter(x => x==='player').length > t.filter(x => x==='ai').length) ? 'PLAYER' : 'AI'
  alert(`Игра окончена! Победил ${winner}`);
  location.reload();
}