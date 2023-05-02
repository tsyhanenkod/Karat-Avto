let part = document.getElementsByClassName('tab-link')
let activePart = document.getElementsByClassName('active-tab')

for (var i=0; i < part.length; i++){

    part[i].addEventListener('click', function(e){

        e.preventDefault();

        if (activePart.length > 0){
            activePart[0].classList.remove('active-tab')
        };
        this.classList.add('active-tab')

        // Получаем id блока, который нужно показать
        let tabId = this.getAttribute('href');

        // Находим блок по id и отображаем его, скрывая остальные
        let tabs = document.querySelectorAll('.tab-pane');
        for (let j = 0; j < tabs.length; j++) {
            tabs[j].classList.remove('show', 'active');
        }
        document.querySelector(tabId).classList.add('show', 'active');
    });
};
