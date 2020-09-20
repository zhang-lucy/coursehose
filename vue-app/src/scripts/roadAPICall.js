// import $ from 'jquery';
export function getRoad(endpoint, course) {
    console.log(endpoint);
    console.log(course);
    return {"Fall 2020": [{name: "6.0001"}], "Spring 2021": [{name: "6.0002"}]}
    // $.post(endpoint, {'course': course}, function(data) {
    //     // assume data is formatted like {semester1: [class1, class2, class3], semester2: [class1, class2], etc.}
    //     return data;
    // });
}
    