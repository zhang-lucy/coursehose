
var courses = new Vue({
    el: '#courses',
    data: {
        courseList: [],
    },
    methods: {
        addCourse: function() {
            var course = $('#courseNumber').val();
            courses.courseList.push(course);
            $('#courseNumber').val('');
        }
    },
});