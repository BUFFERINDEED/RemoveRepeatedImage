# RemoveRepeatedImage
 A  python sctipt used to remove repeated image, based on image hash

## Requirement

* Python (tested with 3.8.0)
* imagehash (tested in 4.1.0)
* pillow (tested with 7.1.2)
  * Recommend install with **pip install pillow**, if you want to remove repeated webp. more details please refer to hint below.
* python-magic (tested with 0.4.18)

**Hint: **

1. Once I was dealing with webp image, with pillow installed by conda, I found I can't open webp directly from Image.open(io.BytesIO(some_bytes_data)), while the pillow installed by pip worked well. I turned out to be the reason of conda didn't dealing with libwebp perfectly.

## Usage

``` shell
python rm_small_image.py --target_path <target_path> --hashType <hashType>
```

Arguments: 

* --target_path: target path, should be directory
* --hashType: should be one item of the following tables. 

| hashType                                                     | hash method        |
| ------------------------------------------------------------ | ------------------ |
| [ahash](http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html) | average hashing    |
| [phash](http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html) | perception hashing |
| [dhash](http://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html) | difference hashing |
| [whash](https://fullstackml.com/2016/07/02/wavelet-image-hash-in-python/) | wavelet hashing    |



## Function

### main()

used to remove repeated image in specified path, will reserve the largest one.



### SearchSameImage(path, searchedFilename, hashType="phash")

used to find all same image to the file corresponding to **searchedFilename**

#### argument: path

the same as --target_path

#### argument: searchedFilename

the very image that you want to search

#### argument: hashType

the same as --hashType



