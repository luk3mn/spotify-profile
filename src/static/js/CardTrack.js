// importScripts "https://kit.fontawesome.com/01edd83a56.js"

class CardTrack extends HTMLElement {
    constructor() {
        super();
        const shadow = this.attachShadow({ mode: "open"});
        // shadow.innerHTML = "<h1>That's my deal</h1>";
        shadow.appendChild(this.build());
        shadow.appendChild(this.styles());
    }

    build() {
        const componentRoot = document.createElement("div")
        componentRoot.setAttribute("class", "card")

        const picture = document.createElement("div")
        picture.setAttribute("class", "picture")

        const cardImage = document.createElement("img")
        cardImage.src = this.getAttribute("image")

        const cardLink = document.createElement("a")
        cardLink.href = this.getAttribute("spotify")
        cardLink.setAttribute("target","_blank")

        const icon = document.createElement("img")
        // icon.setAttribute("class", "fa-solid fa-play")
        icon.src = this.getAttribute("icon")
        cardLink.appendChild(icon)

        picture.appendChild(cardImage)
        picture.appendChild(cardLink)

        const details = document.createElement("div")
        details.setAttribute("class", "details")

        const artist = document.createElement("h4")
        artist.textContent = this.getAttribute("artist")

        const slide = document.createElement("ul")
        slide.setAttribute("class", "slide-info")

        const song = document.createElement("li")
        song.textContent = this.getAttribute("song")
        const album = document.createElement("li")
        album.textContent = this.getAttribute("album")
        const release = document.createElement("li")
        release.textContent = this.getAttribute("release")
        const popularity = document.createElement("li")
        popularity.textContent = this.getAttribute("popularity")
        const played = document.createElement("li")
        played.textContent = this.getAttribute("played")

        slide.appendChild(song)
        slide.appendChild(album)
        slide.appendChild(release)
        slide.appendChild(popularity)
        slide.appendChild(played)

        details.appendChild(artist)
        details.appendChild(slide)

        componentRoot.appendChild(picture)
        componentRoot.appendChild(details)

        return componentRoot;
    }

    styles() {
        const style = document.createElement("style");
        style.textContent = `
            .card {
                display: flex;
                flex-direction: column;

                width: 130px;
                margin: .2rem;
                background-color: var(--bg-third);
                border-radius: 1rem;
                /* border: 3px solid red; */
                
                overflow: hidden;
                position:relative;
                background-color:#333;
                padding: .3rem;
            }
            
            .card .picture {
                /* border: 2px solid white; */
                height: 135px;
            }

            .card .picture a {
                /*border: 2px solid red;*/
                display: flex;
                align-items: center;
                justify-content: center;

                position: relative;
                float: right;
                bottom: 3.3rem;
                right: .5rem;
                font-size: 1.2rem;
                color: var(--bg-primary);
                background-color: var(--bg-secondary);
                padding: 0rem;
                border-radius: 5rem;
                width: 40px;
                height: 40px;
            }

            .card .picture a img {
                width: .8rem;
            }

            .card .picture img {
                width: 100%;
                border-radius: .9rem;
            }

            .card .details h4 {
                font-size: .7rem;
                color: var(--font-primary);
                text-align: center;
                margin: 0;
            }

            .card .details .slide-info {
                width: 100%;
                height:100%;
                position:absolute;
                top: -20px;
                /* right: 0; */
                padding: .5rem;
                right: -200px;
                background-color: var(--bg-third);
                color:#fff;
                transition:0.4s ease;
            }
            
            
            .card .details .slide-info li {
                margin: .4rem 0;
                list-style: none;
                font-size: .7rem;
            }

            .card .details .slide-info li span {
                font-weight: 700;
                /* font-size: .8rem; */
                text-transform: uppercase;
            }

            .card .details:hover .slide-info {
                right: -15px;
            }
        `;

        return style;
    }

}

customElements.define("card-track", CardTrack);