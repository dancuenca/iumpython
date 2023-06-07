with tqdm(total=len(words)) as pbar:
    index = 1
    for word in words:
        el = links(words, word)
        edges += el[0]
        costs += el[1]
        operations += el[2]
        pbar.update(1)
        index += 1

        if index % update_interval == 0:
            progress_bar['value'] = (index / len(words)) * 100
            app.update()

    for word in words:
        el = links(words, word)
        edges += el[0]
        costs += el[1]
        operations += el[2]
        index += 1

        if index % update_interval == 0:
            progress_bar['value'] = (index / len(words)) * 100
            app.update()