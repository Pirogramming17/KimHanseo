const date = new Date(); //현재 날짜 객체 만들기 방법

document.querySelector('.year-month').textContent = '${viewYear+1}년 ${viewMonth}월'//${}는 변수에 접근

const makeCalendat = () => {
    const viewYear = date.getFullYear(); //2022
    const viewMonth = date.getMonth(); //7
    

    //캘린더 년도 달 채우기
    document.querySelector('.year-month').textContent = '${viewYear+1}년 ${viewMonth}월'//${}는 변수에 접근


    //이번 달 마지막 날짜 가져오기
    const thisLast = new Date(viewYear, viewMonth+1, 0); //<< 지정 날짜 객체 만들기
    const thisDate = thisLast.getDate(); // 31
    const thisDay = thisLast.getDay(); // 0

    //저번 달 마지막 날짜 가져오기
    const prevLast = new Date(viewYear, viewMonth, 0);
    const prevDate = prevLast.getDate(); // 30
    const prevDay = prevLast.getDay(); // 4

    //전체 날짜를 만들기 위한 배열 만들기
    const prevDates = [];
    const thisDates = [...Array(thisDate + 1).keys()].slice(1);
    const nextDates = [];

    // 6 = 토요일, 전 달 마지막 요일이 토요일일 경우 그릴 필요가 없다!
    // 이전 달 날짜들을 만들어주는 코드!

    if(prevDay !== 6){
        for(let i=0; i<prevDay+1; i++){
            prevDates.unshift(prevDate - i)
        }
    }

    for(let i=1; i <7-thisDay; i++){
        nextDates.push(i);
    }

    // // ~~~~ 현재과정 ~~~
    // prevDates [26 27 28 29 30]
    // thisDates [1, 2, ~~ 30, 31] 
    // nextDates [1, 2, 3, 4, 5, 6]

    //dates [26 ~~~ 6]

    const dates = prevDates.concat(thisDates, nextDates);



    //div로 감싸서 다시 배열 넣주기
    dates.forEach((date, i) => {
        dates[i] = `<div class="date">${date}</div>`;
    });



    // dates [26 27 28 29 .~~~~~ 1 2 3 4 5 6]
    // dates [<div class="date">26</div>, <div class="date">27</div> ~~~~~~ <div class="date">6</div>]

    
    const firstDateIndex = dates.indexOf(1); //1 요소가 인덱스 몇번에 있는지 알려주는 메소드 indexof
    const lastDateIndex = dates.lastIndexOf(thisDate);
    //투명도를 조절하는 코드
    dates.forEach((date,i) => {

        const condition = i >= firstDateIndex && i< lastDateIndex+1 ? 'this' : 'other'; //삼항 연산자
        
        //if(i >= firstDateIndex && i<lastDateIndex+1) {
        //    const condition = 'this';
        
        //} else {
        //    const condition = 'other';
        //}
    
        dates[i] = `<div class="date"><span class="${condition}"> ${date} </span></div>`


    })

    
    //Dates 그리기
    document.querySelector('.dates').innerHTML = dates.join('');


    //오늘 날짜 그리기
    const today = new Date();
    if(viewYear === today.getFullYear() && viewMonth === today.getMonth()) {
        for(let date of document.querySelectorAll('.this')) {
            if(+date.innerHTML === today.getDate()) {
                date.classList.add('today');
                break;
            }//앞에 +를 붙이면 숫자형으로 인식
        }
    }


}

let date = new Date();
//이전 달로 이동
const prevMont = () => {
    date.setDate(1);//전 달로 날짜 변경
    date.setMonth(date.getMonth()-1)//전 달로 달 변경
    makeCalendat();
}

//이번 달로 이동
const curMonth = () => {
    date = new Date();
    makeCalendat();
}


//다음 달로 이동
const nextMonth = () => {
    date.setDate(1);
    date.setMonth(date.getMonth()+1);
    makeCalendat();
}




