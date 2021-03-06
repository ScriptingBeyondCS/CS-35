// Tabs;
// this is for tabs that pre-load the content;
// no visual styles are associated with the CLASS "tabs";
// this accounts for both vertical and horizontal tabs;
jQuery(function($){

    // loop through each tab widget
    $('div.tabs').each(function(){
        $(this)
            .find('div.tabsNav a')                           // find all the A tags and loop through them;
            .each(function(j){  
                var id = $(this).attr('href').split('#')[1]; // identify the target ID;
                $(this).click(function(){                    // add onClick functionality;
                    $(this)
                        .parents('div.tabs')
                        .find('div.active')                  // find the visible DIVs;
                        .removeClass('active')               // and hide them;
                        .end()
                        .find('div.tabsNav li.active')       // find the 'active' tab;
                        .removeClass('active')               // and remove the active class;
                        .end()
                        .find('div.tabsNav li.off')          // find the 'off' tab (on Horizontal Tabs);
                        .removeClass('off')                  // and remove the off class;
                        .end()
                        .end()
                        .parents('li')
                        .addClass('active')                  // identify this tab as active;
                        .next()                              // add the 'off' class to the next LI;
                        .addClass('off')
                        .blur();
                    $('#' + id).addClass('active');          // show the active tab's DIV;
                    return false;
                });
            });
    });
});

// Legislative Activity Schedule;
// on the homepage;
// JSON content is grabbed through an Ajax call, parsed, and replaces content on the page;
// very similar functionality as the House of Representatives Schedule;
jQuery(function($){
    // function used to parse the JSON content and populate the page;
    function build(obj) {
        if (obj.status != "ok") {
          return;
        }
        var str = '';
        $.each(obj.tr, function(i, td) {
            str = str + '<tr><td>' + td.time + '</td><td>' + td.session + '</td></tr>';
        });
        
        $('div.schedule')
            .find('h2')
            .html(obj.date)      // replace the date title;
            .end()
            .find('table tbody')
            .html(str);          // replace the TBODY (we're not replacing the THEAD);
    }
    
    $('div.schedule')
        .find('div.days_events')
        .append('<a class="scheduleLeft">Previous Sessions</a><a class="scheduleRight">Future Sessions</a>')
        .not('.noleft')
            .find('a.scheduleLeft').show().end()
        .end()
        .not('.noright')
            .find('a.scheduleRight').show().end()
        .end()
        .find('a.scheduleLeft')
        .click(function(){
            // moving back in time;
            var h2 = $(this).parent().find('h2');
            $.get('./legislative/sessions.json.php',           // this URL will change to a dynamic page;
                { currentDate: h2.html(), action:'prev' },            // send the current date to the backend;
                function(data){
                    build(data);                       // call the function to replace the content;
                    $('a.scheduleRight').fadeIn();     // if the other arrow is hidden, show it;
                    if(data.last) {
                        $('a.scheduleLeft').fadeOut(); // if this is the last date with data, prevent the user from clicking this link again;
                    }
                },
                'json');
        })
        .end()
        .find('a.scheduleRight')
        .click(function(){
            // moving forward in time;
            // same comments as the moving back in time piece;
            var h2 = $(this).parent().find('h2');
            $.get('./legislative/sessions.json.php', 
                { currentDate: h2.html(), action:'next' },
                function(data){
                    build(data);
                    $('a.scheduleLeft').fadeIn();
                    if(data.last) {
                        $('a.scheduleRight').fadeOut();
                    }
                },
                'json');
        });
});

// House of Representatives Schedule;
// very similar functionality as the Legislative Activity Schedule;
jQuery(function($){
    // function used to parse the JSON content and populate the page;
    function build(obj) {
        var str = '';
        $.each(obj.tbody, function(i, tr) {
            str = str + '<tr>';
            $.each(tr, function(j, td) {
                // if there is a link, output an A tag, otherwise don't;
                // this could be written with an IIF, but this way is easier to read;
                if (td.link === '') {
                    str = str + '<td class="' + td.clas + '">' + td.day + '</td>';
                }
                else {
                    str = str + '<td class="' + td.clas + '"><a href="' + td.link + '">' + td.day + '</a></td>';
                }
            });
            str = str + '</tr>';
        });
        
        $('div.calendar')
            .find('h1')
            .html(obj.date)      // replace the date title;
            .end()
            .find('table tbody')
            .html(str);          // replace the TBODY (we're not replacing the THEAD);
    }
    
    $('div.calendar')
        .append('<a class="calendarLeft">Previous Month</a><a class="calendarRight">Next Month</a>')
        .find('a.calendarLeft')
        .click(function(){
            // moving back in time;
            var h1 = $(this).parent().find('h1'),
                displayDate = $('#contentMain').find('h2');
            $.get('/legislative/cal.json.php?action=prev',          // this URL will change to a dynamic page;
                { currentDate: h1.html() , displayDate: displayDate.html() },            // send the current date to the backend;
                function(data){
                    build(data);                       // call the function to replace the content;
                    $('a.calendarRight').fadeIn();     // if the other arrow is hidden, show it;
                    if(data.last == 'true') {
                        $('a.calendarLeft').fadeOut(); // if this is the last date with data, prevent the user from clicking this link again;
                    }
                },
                'json');
        })
        .end()
        .find('a.calendarRight')
        .click(function(){
            // moving forward in time;
            // same comments as the moving back in time piece;
            var h1 = $(this).parent().find('h1'),
                displayDate = $('#contentMain').find('h2');
            $.get('/legislative/cal.json.php?action=next', 
                { currentDate: h1.html() , displayDate: displayDate.html() },
                function(data){
                    build(data);
                    $('a.calendarLeft').fadeIn();
                    if(data.last == 'true') {
                        $('a.calendarRight').fadeOut();
                    }
                },
                'json');
        });
});

// Vertical Tabs;
// this just adds a minimum height to the content area, dont want the content to be shorter than the navigation;
jQuery(function($){
    $('div.tabsVertical').each(function(){
        var height = $(this).find('div.tabsNav').height();
        $(this)
            .find('div.tabsBody')
            .css('min-height', height + 'px');
        
        if(navigator.userAgent.match(/msie [6]/i)) {
            $(this)
                .find('div.tabsBody')
                .css('height', height + 'px');
        }
    });
});

// Form highlights;
jQuery(function($){
    $('#nav input')
        .focus(function(){
            $(this).parents('form').addClass('focus');
        })
        .blur(function(){
            $(this).parents('form').removeClass('focus');
        });
    $('div.form input')
        .focus(function(){
            $(this).parents('div.form').addClass('focus');
        })
        .blur(function(){
            $(this).parents('div.form').removeClass('focus');
        });
});

// Congressional Art Competition State Form/Navigation;
// JS hides the submit button, and adds on onChange event to submit the form;
jQuery(function($){
    $('div.entries form')
        .find('input[class=goTo]')
        .hide()
        .end()
        .find('select')
        .change(function(){
            $(this).parents('form').submit(); // submit the form when the user changes the SELECT;
        })
        .end()
        .submit(function(){
            // PLACEHOLDER;
            // used to test the form submission;
            //alert('This form is submitted on-change of the State SELECT field.');
            //return false;
            var dest = $(this).find("option:selected").attr("value");
            if (dest !== "") {
                    window.location=$(this).find("option:selected").attr("value");
            }
            return false;
        });
});

//	Home page list of Representatives
//	JS provides link to Rep's site
jQuery(function($){
    $('div#representatives form:first')
        .submit(function(){
            var dest = $(this).find("option:selected").attr("value");
            if (dest !== "") {
                    window.location.href=$(this).find("option:selected").attr("value");
            }
            return false;
        });
});

// Carousels;
jQuery(function($){
    // loop through each carousel;
    $('div.carousel').each(function(i){
        // assign a unique id (allows for multiple per page);
        var id = 'carouselContainer' + i;
        
        var carousel = {
            // slideshow navigation (pagination);
            nav: '<div class="carouselNav"><div class="carouselNavPager"></div></div>',
            // settings for the cycle plugin;
            config: {
                fx:               'scrollHorz',                       // name of transition effect (or comma separated names, ex: fade,scrollUp,shuffle);
                speed:            1000,                               // speed of the transition (any valid fx speed value);
                timeout:          0,                                  // milliseconds between slide transitions (0 to disable auto advance);
                pager:            '#' + id + ' div.carouselNavPager', // selector for element to use as pager container;
                prev:             '#' + id + ' a.carouselNavPrev',    // selector for element to use as click trigger for previous slide;
                next:             '#' + id + ' a.carouselNavNext',    // selector for element to use as click trigger for next slide;
                activePagerClass: '#' + id + ' active'                // class name used for the active pager link;
            }
        };
        
        // add the necessary HTML and initialize the cycle plugin;
        $(this)
            .wrap('<div class="carouselContainer" id="' + id + '"></div>') // wrap the slideshow in a container;
            .after(carousel.nav)                                           // add the navigation to the container;
            .cycle(carousel.config)                                        // initialize the cycle plugin;
            .find('div.moduleCarousel')
            .hover(                                                        // add Hover interaction;
                function(){
                    $(this).addClass('hover');
                },
                function(){
                    $(this).removeClass('hover');
                }
            );
            
    });
});

// Home Page rotator;
jQuery(function($){
    // loop through each slider
    $('#homepage_features').cycle({
			fx:               'scrollHorz',                // name of transition effect (or comma separated names, ex: fade,scrollUp,shuffle) 
			speed:            500,                      // speed of the transition (any valid fx speed value) 
			timeout:          8000,                           // milliseconds between slide transitions (0 to disable auto advance) 
			pause:            true,                        // true to enable "pause on hover" 
			slideExpr:		  '.tabsBody',
			pager:			  '#homepage_features .tabsNav ul',
			activePagerClass: 'active',
			pagerAnchorBuilder: function(idx,slide) {
				return '#homepage_features .tabsNav li:eq(' + idx + ') a';
			}
	});
});

// Sliders;
jQuery(function($){
    // loop through each slider
    $('div.slider').each(function(i){
        // assign a unique id
        var id = 'sliderContainer' + i;
        
        var slider = {
            // slideshow navigation (pagination)
            nav: '<div class="sliderNav"></div>',
            // settings for the cycle plugin
            config: {
                fx:               'scrollHorz',                // name of transition effect (or comma separated names, ex: fade,scrollUp,shuffle) 
                speed:            'fast',                      // speed of the transition (any valid fx speed value) 
                timeout:          5000,                           // milliseconds between slide transitions (0 to disable auto advance) 
                pager:            '#' + id + ' div.sliderNav', // selector for element to use as pager container 
                pause:            true,                        // true to enable "pause on hover" 
                activePagerClass: 'active'                     // class name used for the active pager link 
            }
        };
        
        $(this)
            .wrap('<div class="sliderContainer" id="' + id + '"></div>') // wrap the slideshow in a container
            .after(slider.nav)                                           // add the navigation to the container
            .cycle(slider.config);                                       // initialize the cycle plugin
    });
});

// Hidden LABELs;
jQuery(function($){
    $('label.hide').each(function(i){                      // loop through each LABEL to hide;
        var obj = '#' + $(this).attr('for');               // find the TARGET form field;
        var val = $(this).html();                          // record the LABEL value/html;
        if($(obj).size() > 0) {
            if($(obj).get(0).tagName == 'INPUT') {         // if this form field is an INPUT (don't care about SELECTs);
                if($(obj).attr('value') === '') {
                    $(obj).attr('value', val);
                }
                $(obj)
                    .focus(function(){
                        if($(this).attr('value') == val){
                            $(this).attr('value', '');
                        }
                    })
                    .blur(function(){
                        if($(this).attr('value') == ''){
                            $(this).attr('value', val);
                        }
                    });
            }
            $(this).hide();                                // hide the LABEL once the value is in the form field;
        }
    });
});

// Lightboxes;


jQuery(function($){
    $('div.slider').each(function(i){
        $(this).find('div.moduleBody a').lightBox({
            overlayBgColor       : '#333',
            overlayOpacity       : 0.6,
            imageBlank           : '/content/static/img/lightbox/blank.gif',
            imageLoading         : '/content/static/img/lightbox/loading.gif',
            imageBtnClose        : '/content/static/img/lightbox/close.gif',
            imageBtnPrev         : '/content/static/img/lightbox/prev.gif',
            imageBtnNext         : '/content/static/img/lightbox/next.gif',
            containerResizeSpeed : 350,
            txtImage             : 'Image',
            txtOf                : 'of'
        });
    });
});




// IE class fixes
jQuery(function($){
	if (/MSIE (\d+\.\d+);/.test(navigator.userAgent)){ //test for MSIE x.x;
	  var ieversion=new Number(RegExp.$1) // capture x.x portion and store as a number
	  if (ieversion < 8) {
            $('input').each(function(){
                var clas = $(this).attr('type');
                $(this).addClass(clas);
            });
            $('li:first-child').addClass('first-child');
      }
	  else if (ieversion == 8) {
            $('body').addClass('ie8');
   	  }
	}
});


