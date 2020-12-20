
            var chart = Highcharts.chart('container', {
            chart: {
                spacing : [20, 0 , 20, 0]
            },
            title: {
                floating:true,
                text: '用户偏好分析'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: true,
                        format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                        style: {
                            color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                        }
                    },
                    point: {
                        events: {
                            mouseOver: function(e) {  // 鼠标滑过时动态更新标题
                                // 标题更新函数，API 地址：https://api.hcharts.cn/highcharts#Chart.setTitle
                                chart.setTitle({
                                    text: e.target.name+ '\t'+ e.target.y + ' 人'
                                });
                            }
                            //,
                            // click: function(e) { // 同样的可以在点击事件里处理
                            //     chart.setTitle({
                            //         text: e.point.name+ '\t'+ e.point.y + ' %'
                            //     });
                            // }
                        }
                    },
                }
            },
            series: [{
                type: 'pie',
                innerSize: '80%',
                name: '占比',
                data: [
                    {name:'Like',   y: parseInt('{{trailer.likeCount|safe }}'), url : 'http://bbs.hcharts.cn'},
                    ['Favorite',       parseInt('{{trailer.favoriteCount|safe }}')],
                    {
                        name: 'Dislike',
                        y: parseInt('{{trailer.dislikeCount|safe }}'),
                        sliced: true,
                        selected: true,
                        url: 'http://www.hcharts.cn'
                    },
                ]
            }]
        }, function(c) { // 图表初始化完毕后的会掉函数
            // 环形图圆心
            var centerY = c.series[0].center[1],
                titleHeight = parseInt(c.title.styles.fontSize);
            // 动态设置标题位置
            c.setTitle({
                y:centerY + titleHeight/2
            });
        });