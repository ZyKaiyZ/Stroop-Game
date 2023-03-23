const vm = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            fontColor: 'black',
            colorText:"藍色",
            correct: 0,
            fail: 0,
            done: 0,
            timer: 0
        }
    },
    methods:{
        red: function(){
            this.checkAnswer("紅色")
        },
        blue: function(){
            this.checkAnswer("藍色")
        },
        green: function(){
            this.checkAnswer("綠色")        
        },
        black: function(){
            this.checkAnswer("黑色")
        },
        yellow: function(){
            this.checkAnswer("黃色")
        },
        showAlert(bottonText){
            swal({
                title: 'Stroop Game',
                icon: "success",
                content: {
                    element: "input",
                    attributes: {
                      placeholder: "輸入計時秒數"
                    }
                },
                button: {
                  text: bottonText,
                },
                closeOnClickOutside: false,
            }).then((value) => {
                this.countdown(value);
                this.correct = 0, this.fail = 0, this.done = 0;
            });
        },
        checkAnswer(colorParam){
            var textArray = ["紅色","藍色","綠色","黑色","黃色"];
            var colorArray = ["red","blue","green","black","rgb(203, 203, 0)"];
            var r = Math.floor(Math.random() * 5);
            this.colorText = textArray[r];
            console.log(this.fontColor);
            textArray[colorArray.indexOf(this.fontColor)] == colorParam ? this.correct++ : this.fail++;
            this.done = this.correct + this.fail;
            this.getRandomColor()
        },
        getRandomColor(){
            var colorArray = ["red","blue","green","black","rgb(203, 203, 0)"];
            var r = Math.floor(Math.random() * 5);
            this.fontColor = colorArray[r];
        },
        countdown(seconds) {
            var interval = setInterval(()=>{
                this.timer = seconds;
                if(--seconds < 0){
                    clearInterval(interval);
                    this.showAlert("R e s t a r t")
                }
            }, 1000);
        }
    },
    mounted(){
        this.showAlert("S t a r t")
    }
}).mount('#app')