//(function(){
//    window.showhideonclick = function(class_selector){
//        var el = document.body.querySelector(class_selector);
//        if(el.style.display == 'none'){
//            el.style.display = 'block';
//        }
//        else if(el.style.display == 'block'){
//            el.style.display = 'none';
//        }
//    }
//    window.showMenu = function(class_selector){
//        var el = document.body.querySelector(class_selector);
//        el.style.display = 'block';
//        setTimeout(function(){
//            hideMenu(class_selector);
//        }, 5000);
//    }
//    window.hideMenu = function(class_selector){
//        var el = document.body.querySelector(class_selector);
//        el.style.display = 'none';
//    }
//})(window);

(function(){
    var popupTrigger = function(trigger_name, target_name){
        var trigger = document.querySelector('.' + trigger_name);
        trigger.onmouseover = function(evnt){
            var target = document.querySelector('.' + target_name);
            if(target.hasOwnProperty('isActive') && target.isActive == false){
                target.isActive = true;
                target.style.display = 'block';
            }
            else if(!target.hasOwnProperty('isActive')){
                target.isActive = true;
                target.style.display = 'block';
            }
        }
        var target = document.querySelector('.' + target_name);
        target.onmouseout = function(evnt){
            this.isActive = false;
        }
        target.onmouseover = function(evnt){
            if(target.timer !== undefined){
                clearTimeout(target.timer);
            }
            target.timer = setTimeout(function(){
                if(target.isActive == false){
                    target.style.display = 'none';
                }
            }, 2000);
        };
        trigger.onmouseout = function(){
            target.isActive = false;
            target.timer = setTimeout(function(){
                if(!target.isActive){
                    target.style.display = 'none';
                }
            }, 2000);
        }
    }
    this.onload = function(){
        popupTrigger.call(this, 'js-popup-info', 'js-hidden-info');
        popupTrigger.call(this, 'js-popup-portfolio', 'js-hidden-portfolio');
    }
}).call(this)