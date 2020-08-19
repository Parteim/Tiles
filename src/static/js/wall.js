// import(tileHTML)

class Wall {
    main = document.getElementsByTagName('main')[0];
    wall = document.getElementById('wall');
}

class Tile {
    element = document.createElement('li');
    header = document.createElement('header');
    tileAuthorImgContainer = document.createElement('div');
    tileAuthorImg = document.createElement('img');
    tileAuthor = document.createElement('h3');
    tileContent = document.createElement('div');

    static revealFlag = false

    id = NaN;
    type = NaN;
    contentElements = [];
    author = {
        username: 'Some Username',
        imagePath: '/static/img/user-3.jpg',
    };

    createTile() {
        this.element.className = 'tile ';
        this.element.id = this.id;
        this.header.className = 'tile_header';
        this.tileAuthorImgContainer.className = 'tile_author_img_container';
        this.tileAuthorImg.className = 'tile_author_img';
        this.tileAuthor.className = 'tile_author';
        this.tileContent.className = 'tile_content';

        if (this.type) {
            this.element.className += this.type;
        }

        this.element.appendChild(this.header);
        this.element.appendChild(this.tileContent);
        this.tileAuthorImgContainer.appendChild(this.tileAuthorImg);
        this.header.appendChild(this.tileAuthorImgContainer);
        this.header.appendChild(this.tileAuthor);

        this.tileAuthor.innerHTML = '<span>'+ this.author.username +'</span>';
        this.tileAuthorImg.src = this.author.imagePath;

        for (let contentElement in this.contentElements) {
            let newElement = document.createElement('div');
            newElement.className = 'tile_content_element';
            this.tileContent.appendChild(newElement);
        }

    }

    constructor(id, type, contentElements, user) {
        this.id = id;
        this.type = type;
        this.contentElements = contentElements;
        // this.author.username = user.username;
        // this.author.imagePath = user.image;

        console.log(this.type);

        this.createTile();

    }

    draw(obj) {
        let wall = document.getElementById('wall');
        wall.appendChild(this.element);

        this.element.addEventListener("click", function () {
            if (!Tile.revealFlag) {
                obj.reveal();
                Tile.revealFlag = true;
            }
        })
    }

    reveal() {
        let body = document.getElementsByTagName('body')[0];
        let main = document.getElementsByTagName('body')[0];
        let revealTile = document.createElement('div');
        let element = this.element;

        function revealTileContent() {
            let tileBar = document.createElement('div');
            let rollDownBtn = document.createElement('button');
            let closeBtn = document.createElement('button');

            tileBar.className = 'reveal-tile-bar';
            rollDownBtn.id = 'tile-roll-down-btn';
            closeBtn.id = 'tile-close-btn';

            revealTile.appendChild(tileBar);
            tileBar.appendChild(rollDownBtn);
            tileBar.appendChild(closeBtn);
            rollDownBtn.innerHTML = '<i class="fas fa-minus"></i>';
            closeBtn.innerHTML = '<i class="fas fa-times"></i>';

            closeBtn.addEventListener("click", function () {
                appear();
                setTimeout(function () {
                    revealTile.remove();
                    document.getElementsByTagName('html')[0].style.overflow = '';
                    Tile.revealFlag = false;
                }, 600);
            });
        }

        function appear() {
            revealTile.style.transition = 'all .5s';
            revealTile.className = '';
            revealTile.style.top = element.getBoundingClientRect().y + 'px';
            revealTile.style.left = element.getBoundingClientRect().x + 'px';
            revealTile.style.width = element.getBoundingClientRect().width + 'px';
            revealTile.style.height = element.getBoundingClientRect().height + 'px';
            revealTile.style.borderRadius = '10px';
            revealTile.style.backgroundColor = '#1b756d';
            revealTile.style.position = 'fixed';
        }

        function reveal() {
            revealTile.className = 'reveal-tile';
            revealTile.style.top = '50%';
            revealTile.style.left = '50%';
            revealTile.style.width = '90%';
            revealTile.style.height = '90%';
            revealTile.style.borderRadius = '20px';
            revealTile.style.backgroundColor = '#1b756d';
        }

        document.getElementsByTagName('html')[0].style.overflow = 'hidden';

        revealTileContent();

        appear(this.element);

        setTimeout(reveal, 200);

        body.appendChild(revealTile);

    }

}

for (let i = 0; i < 3; i++) {
    let tile = new Tile(i, 'medium-tile', [1, 2, 3])
    tile.draw(tile)
}