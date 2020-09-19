
var courses = new Vue({
    el: '#courses',
    data: {
        courseList: [],
    },
    methods: {
        addCourse: function() {
            var course = $('#courseNumber').val();
            var courseItem;
            if (course.toString() in classes) {
                courseItem = {number: course, name: classes[course.toString()]['n']};
            } else {
                courseItem = {number: course, name: "No Class Found"};
            }

            // TODO trying to not allow duplicate classes but accessing courseList gives weird behavior sigh
            var courseSet = new Set();
            for (c in this.courseList) {
                courseSet.add(c.name); // this breaks sadly I hate Vue
            }
            if (!(courseSet.has(course))) {
                this.courseList.push(courseItem);
                this.courseList.sort((a, b) => a.number - b.number);
            }
            $('#courseNumber').val('');
        },

        deleteCourse: function(course) {
            this.courseList.splice(this.courseList.indexOf(course), 1);
        },
    },
});
