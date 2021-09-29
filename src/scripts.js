new Vue({
    el: '#app',
    data: {
        isBurgerActive: false,
        sections: {}
    },
    created: async function() {
        // try {
        //     const sectionsRes = await fetch('./data.json');
        //     this.sections = await sectionsRes.json();
        // } catch (e) {
        //     console.error(e);
        // }
    }
})