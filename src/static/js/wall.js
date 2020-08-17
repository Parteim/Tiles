// import(tileHTML)

class Wall {
    main = document.getElementsByTagName('main')[1];
    wall = document.getElementById('wall');
}

class Tile {
    element = document.createElement('li');
    header = document.createElement('header');
    tileAuthorImgContainer = document.createElement('div');
    tileAuthorImg = document.createElement('img');
    tileAuthor = document.createElement('h3');
    tileContent = document.createElement('div');

    id = NaN;
    type = NaN;
    contentElements = [];
    author = {
        username: NaN,
        imagePath: NaN,
    };

    createTile() {

        this.element.className = 'tile ';
        this.header.className = 'tile_header';
        this.tileAuthorImgContainer.className = 'tile_author_img_container';
        this.tileAuthorImg.className = 'tile_author_img';
        this.tileAuthor.className='tile_author';
        this.tileContent.className='tile_content';

        for (let contentElement in this.contentElements) {

        }

        this.element.appendChild(this.header);
        this.tileAuthorImgContainer.appendChild(this.tileAuthorImg)
        this.header.appendChild(this.tileAuthorImgContainer);
        this.header.appendChild(this.tileAuthor);

    }

    constructor(id, type, contentElements, username, imagePath) {
        this.id = id;
        this.type = type;
        this.contentElements = contentElements;
        this.author.username = username;
        this.author.imagePath = imagePath;

        if (this.type) {
            this.element.className += this.type;
        }
    }

    draw() {
        let wall = document.getElementById('wall');
        wall.appendChild(this.element);
    }

    reveal() {
        let main = document.getElementsByTagName('main')[0]
        let revealTile = document.createElement('div')

        revealTile.className = 'reveal-tile'
    }

}

let tile = new Tile(1, 'large-tile')

tile.draw()